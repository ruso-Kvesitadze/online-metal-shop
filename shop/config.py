from os import path


class Config(object):
    SECRET_KEY = "mysectretkey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(BASE_DIRECTORY, 'db.sqlite')
    MAIL_SERVER ='sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '7fa3a62c4f1a24'
    MAIL_PASSWORD = 'f9b1bb7e872c2e'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    FLASK_ADMIN_SWATCH = "slate"

class Constant:
    SERIALIZER_SALT = "12345678"