# -*- coding: utf-8 -*-

"""
所有的插件，只是生成，初始化统一放到application里
"""

from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

db = SQLAlchemy()
admin = Admin(template_mode='bootstrap3')
login_manager = LoginManager()
