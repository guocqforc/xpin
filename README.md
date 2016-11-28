# xpin
内部统一认证


### app

config 需要配置


    SECRET_KEY = 'tmp_secret_key'

    # flask-sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite')
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_dpl'

    CLIENT_SECRET = '323'

    DING_CORP_ID =
    DING_CORP_SECRET =
    DING_AGENT_ID =

    SEND_CLOUD_API_USER =
    SEND_CLOUD_API_KEY =
    SEND_CLOUD_SENDER =
