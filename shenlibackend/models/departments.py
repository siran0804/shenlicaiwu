# -*- coding: utf-8 -*-
# @Time : 2021/10/18 10:18 am
# @Author : taonian@nj.iscas.ac.cn
# @File : publish.py

import datetime
from flask import current_app
from shenlibackend import db
from shenlibackend.utils.shenliexceptions import *
from shenlibackend.utils.snowflake import id_generator
from shenlibackend.models.basemodel import BaseModel


class Departments(BaseModel):
    """
    model of department
    """
    __tablename__ = "departments"
    id = db.Column(db.BigInteger, primary_key=True)  # 使用Snowflake生成ID
    name = db.Column(db.String(256))
    idlink = db.Column(db.String(1024))
    parent = db.Column(db.BigInteger, index=True)
    pname = db.Column(db.String(512))


