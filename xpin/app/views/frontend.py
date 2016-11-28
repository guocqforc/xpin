#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import datetime
import json

from flask import Blueprint
from flask import render_template, jsonify
from flask import request, current_app, g

from ... import constants
from ...log import logger
from ..models import Pin, User
from ..extensions import db

bp = Blueprint('frontend', __name__)


@bp.before_request
def unpack_input():
    for key in ('data', 'sign'):
        if key not in request.values:
            return jsonify(
                ret=constants.RET_PARAMS_INVALID
            )

    client_secret = current_app.config['CLIENT_SECRET']

    my_sign = hashlib.md5('|'.join(
        [client_secret, request.values['data']]
    )).hexdigest()

    if my_sign != request.values['sign']:
        return jsonify(
            ret=constants.RET_SIGN_INVALID
        )

    try:
        g.input = json.loads(request.values['data'])
    except:
        logger.error('json loads fail. request: %s', request)
        return jsonify(
            ret=constants.RET_PARAMS_INVALID
        )


@bp.route(constants.URL_PIN_CREATE)
def create_pin():

    for key in ('username', 'source'):
        if key not in g.input:
            return jsonify(
                ret=constants.RET_PARAMS_INVALID
            )

    username = g.input['username']
    source = g.input['source']

    user = User.query.filter(User.username == username).first()

    if not user or not user.valid:
        return jsonify(
            ret=constants.RET_USER_INVALID,
        )

    # 删掉旧的
    Pin.query.filter(
        Pin.user_id == user.id,
        Pin.source == source,
    ).delete()

    db.session.commit()

    pin = Pin()
    pin.user_id = user.id
    pin.source = source
    pin.code = Pin.create_code(current_app.config['PIN_LENGTH'])

    if current_app.config['PIN_MAX_AGE']:
        pin.expire_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=current_app.config['PIN_MAX_AGE'])

    db.session.add(pin)
    db.session.commit()

    return jsonify(
        ret=0,
        pin=pin.code,
    )
