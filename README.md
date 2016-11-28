# xpin
内部统一认证


### app

config 需要配置


    SECRET_KEY = 'tmp_secret_key'

    # flask-sqlalchemy
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite')
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/flask_dpl'

