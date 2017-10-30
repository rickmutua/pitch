class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://erick:qwerty12345@localhost/pitch'


class ProdConfig(Config):

    pass


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://erick:qwerty12345@localhost/pitch'

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}