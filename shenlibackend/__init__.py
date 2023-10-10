# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from config import config_map

db = SQLAlchemy()
jwt = JWTManager()
redis_store = None
print('test oneline deploy')


# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name:
    :return:
    """
    app = Flask(__name__, static_folder='static')
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    jwt.init_app(app)
    db.init_app(app)
    CORS(app, supports_credentials=True)
    global redis_store

    # 注册蓝图
    from shenlibackend import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1/")

    return app
