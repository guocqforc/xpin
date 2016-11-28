# -*- coding: utf-8 -*-

import datetime
import re

from passlib.hash import sha256_crypt
from sqlalchemy.types import TypeDecorator, TEXT
from flask_login import UserMixin

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
        return u'%s' % self.username

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


class User(UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    login_time = db.Column(db.DateTime)
    roles = db.Column(ListType)
