# -*- coding: utf-8 -*-

import os
import smtplib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'tmp_secret_key'

# flask-sqlalchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite')


CLIENT_SECRET = '123'

PIN_LENGTH = 6
PIN_MAX_AGE = 300
PIN_MAX_TRY_TIMES = 5
PIN_LOG = False

DING_CORP_ID = ''
DING_CORP_SECRET = ''
DING_AGENT_ID = ''

# 可选
SEND_CLOUD_API_USER = ''
SEND_CLOUD_API_KEY = ''
SEND_CLOUD_SENDER = ''

# 可选
MAIL_SEND_LIST = [
    {
        'host': 'smtp.qq.com',
        'port': smtplib.SMTP_PORT,  # smtplib.SMTP_SSL_PORT
        'username': 'xxx@qq.com',
        'password': 'xxxx',
        'sender': 'xxx@qq.com',
        'use_ssl': False,
        'use_tls': False,
    }
]
