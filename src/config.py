from distutils.debug import DEBUG
from msilib.schema import Class
from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')


class DevelpmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelpmentConfig
}