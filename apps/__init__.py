#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'
from flask import Flask
import setting
from exts import db
from apps.user.view import user_bp
def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(setting.DevelopmentConfig)
    #初始化配置db
    db.init_app(app=app)
    #注册蓝图
    app.register_blueprint(user_bp)
    return app