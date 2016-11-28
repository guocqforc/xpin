# -*- coding: utf-8 -*-

NAME = 'xauth'

# URL 定义

# 验证用户是否有效
URL_USER_VERIFY = '/user/verify'

# 发送PIN码
URL_USER_PIN_SEND = '/user/pin/send'

# 验证用户PIN
URL_USER_PIN_AUTH = '/user/pin/auth'


# 返回码定义

# 内部错误
RET_INTERNAL = -1000

# 用户无效
RET_USER_INVALID = 1000

# PIN无效
RET_USER_PIN_VALID = 2000


# 默认app配置
CONFIG = dict(
    BLUEPRINTS=(
        ('views.frontend', ''),
    ),

    # flask-sqlalchemy
    SQLALCHEMY_ECHO=False,

    # admin_user
    SESSION_KEY_ADMIN_USERNAME='admin_username',
)

