import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'supersecretkey'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@db/dishes_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'


class Prod(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')


class Dev(Config):
    DEBUG = True
    HOST = "0.0.0.0"


class Test(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@db_test/dishes_db_test'
