# -*- coding: utf-8 -*-

from importlib import import_module
from flask import Flask
from flask import request

from extensions import db, admin
import models
import views.admin


def create_app(config, name=None):
    if not name:
        name = __name__

    app = Flask(name)

    app.config.from_object(config)

    configure_logging(app)
    configure_extensions(app)
    configure_context_processors(app)
    configure_handlers(app)
    configure_views(app)

    return app


def configure_logging(app):
    import logging.config

    app.logger and logging.config.dictConfig(app.config['LOGGING'])


def configure_extensions(app):
    """
    初始化插件
    """
    db.init_app(app)

    admin.init_app(app)


def configure_context_processors(app):
    """
    模板变量
    """
    pass


def configure_handlers(app):
    """
    before_request之类的处理
    """
    pass


def configure_views(app):
    """
    注册views
    """
    # 注册 admin views
    views.admin.register_views(app)

    for it in app.config['BLUEPRINTS']:
        app.register_blueprint(import_module(it[0]).bp, url_prefix=it[1])
