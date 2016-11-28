# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# flask-sqlalchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite')

