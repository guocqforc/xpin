# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = 'tmp_secret_key'

# flask-sqlalchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite')


CLIENT_SECRET = '123'

DING_CORP_ID = ''
DING_CORP_SECRET = ''
DING_AGENT_ID = ''

# 可选
SEND_CLOUD_API_USER = ''
SEND_CLOUD_API_KEY = ''
SEND_CLOUD_SENDER = ''
