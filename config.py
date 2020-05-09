class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dynamo:den28041997is@localhost/blog'
    DEBUG=True

class TestConfig(Config):
    pass

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}