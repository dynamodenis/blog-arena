import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    RANDOM_API='http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dynamo:den28041997is@localhost/blogs'
    DEBUG=True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dynamo:den28041997is@localhost/test_blog'

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}