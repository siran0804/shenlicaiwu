# coding:utf-8

from logging.config import dictConfig
import os

log_config = {
    'version': 1,
    'root': {
        'level': 'INFO',
        'handlers': ['portal_handle']
    },

    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        },
        "portal_handle": {
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": 1024 * 1024,
            "backupCount": 1,
            "encoding": "utf-8",
            "level": "INFO",
            "formatter": "default",
            "filename": 'logs/shenlibackend.logs',
        },
    },
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in [%(filename)s:%(lineno)s]: %(message)s',
        },
        'simple': {
            'format': '%(asctime)s - %(levelname)s - %(message)s'
        }
    },
}
dictConfig(log_config)


class Config(object):
    DEBUG = True
    DISP_NUM = 3
    SECRET_KEY = "sadfef0*sd"
    JWT_SECRET_KEY = "sdafader000"
    JWT_TOKEN_LOCATION = ['headers']
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60 * 24

    SQLALCHEMY_ECHO = True

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # 域名


class DevelopmentConfig(Config):
    """
    开发模式
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:0804@127.0.0.1:3306/shenlicaiwu'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = 1800
    RDEPT = 7110024143076200452


class ProductionConfig(Config):
    """
    生产环境配置信息
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:0804@127.0.0.1:3306/shenlicaiwu'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 30
    SQLALCHEMY_POOL_RECYCLE = 1800
    RDEPT = 7110024143076200452


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}
