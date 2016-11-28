#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import json

from flask import Blueprint
from flask import render_template, jsonify
from flask import request, current_app, g

from ... import constants
from ...log import logger
from ..models import Pin, User

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

    username = g.input.get('username')
    if not username:
        return jsonify(
            ret=constants.RET_PARAMS_INVALID
        )

    user = User.query.filter(User.username == username).first()

    return jsonify(
        ret=0,
        pin='ok',
    )
