import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    # Statement for enabling the development environment
    DEBUG                   = True
    DEVELOPMENT             = True

    # Secret for signing cookies
    SECRET_KEY              = "UmVkQnVsbE1pY3JvcGhvbmVIZWFkc2V0TGFtcERlc2syMDgwVGkK"
    
    # Enable Protection against Cross Site Request Forgery (CSRF)
    CSRF_ENABLED            = True
    CSRF_SESSION_KEY        = "QmF0dGVyeUhvcnNlU3RhcGxlUmVkQnVsbEtleWJvYXJkCg=="

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    FLASK_ENV               = 'production'

    DEVELOPMENT             = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app/database/production.db')

    X_ADMIN_PASSWORD        = 'StrongPasswordHere'

class DevelopmentConfig(Config):
    FLASK_ENV               = 'development'
    TESTING                 = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app/database/development.db')

    X_ADMIN_PASSWORD   = 'admin'


class TestingConfig(Config):
    FLASK_ENV           = 'testing'

    TESTING             = True
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO         = True