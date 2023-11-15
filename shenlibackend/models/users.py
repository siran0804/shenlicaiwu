# -*- coding: utf-8 -*-
# @Time : 2021/10/18 10:18 am
# @Author : taonian@nj.iscas.ac.cn
# @File : publish.py

import datetime
from flask import current_app
from shenlibackend import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from shenlibackend.utils.shenliexceptions import *
from shenlibackend.utils.snowflake import id_generator
from shenlibackend.models.basemodel import BaseModel


class User(UserMixin, BaseModel):
    """
    user base model, not create table
    """
    __tablename__ = "user"
    # id = db.Column(UUID(as_uuid=True), primary_key=True, server_default=sa_text("uuid_generate_v4()"))
    id = db.Column(db.BigInteger, primary_key=True)  # 使用Snowflake生成ID

    username = db.Column(db.String(64), index=True)
    phone = db.Column(db.String(11), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    id_card_num = db.Column(db.String(18), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    role = db.Column(db.BigInteger)
    dept = db.Column(db.BigInteger)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def change_pwd(self, old_pwd, new_pwd):
        if self.verify_password(old_pwd):
            self.password_hash = generate_password_hash(new_pwd)
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                current_app.logger.error(str(e))
                raise ServerError
        else:
            raise PasswordError

    def reset_pwd(self, new_pwd):
        self.password_hash = generate_password_hash(new_pwd)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(str(e))
            raise ServerError


class Roles(BaseModel):
    """
    role table
    """
    __tablename__ = 'roles'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(64))
    dispname = db.Column(db.String(64))
    permission = db.Column(db.String(64))









