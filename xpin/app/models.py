# -*- coding: utf-8 -*-

import datetime
import re
import random

from passlib.hash import sha256_crypt
from sqlalchemy.types import TypeDecorator, TEXT
from sqlalchemy import UniqueConstraint

from extensions import db


class ListType(TypeDecorator):
    impl = TEXT

    def process_bind_param(self, value, dialect):
        return ','.join(value or [])

    def process_result_value(self, value, dialect):
        return re.split(r'\s*,\s*', value or '')


class AdminUser(db.Model):
    """
    user基类
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    login_time = db.Column(db.DateTime)
    roles = db.Column(ListType)

    def __unicode__(self):
        return u'<%s %s>' % (type(self).__name__, self.username)

    def set_password(self, raw_password):
        """设置密码，要加密"""
        self.password = sha256_crypt.encrypt(raw_password)

    def check_password(self, raw_password):
        """检查密码是否合法"""
        return sha256_crypt.verify(raw_password, self.password)

    @classmethod
    def auth(cls, username, raw_password):
        """验证用户登录。如果登录成功，返回用户"""
        obj = cls.query.filter_by(username=username).first()

        if obj and obj.check_password(raw_password):
            return obj
        else:
            return None


class User(db.Model):
    """
    用户配置
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    ding_id = db.Column(db.String(255), nullable=False)
    mail = db.Column(db.String(255), nullable=True)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __unicode__(self):
        return u'<%s %s>' % (type(self).__name__, self.username)


class Pin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    source = db.Column(db.Integer, nullable=False)
    code = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    user = db.relationship('User', backref=db.backref('pins', order_by=db.desc(create_time)))

    __table_args__ = (
        UniqueConstraint('user_id', 'source', 'pin', name='_user_source_pin'),
    )

    @classmethod
    def create_code(cls, length):
        """
        创建code
        :return:
        """

        chars = '0123456789'
        return ''.join([random.choice(chars) for i in xrange(length)])

    def __unicode__(self):
        return u'<%s %s-%s-%s>' % (type(self).__name__, self.user_id, self.source, self.code)
