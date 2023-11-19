# -*- coding: utf-8 -*-

from functools import wraps
from shenlibackend import jwt
from shenlibackend.utils.shenliexceptions import *
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from shenlibackend.models.users import Roles

from manager import app


def error_handler(error):
    response = jsonify({
        'msg': error.msg,
        'code': error.error_code,
        'display': error.display
    })

    return response


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return error_handler(MissAuthorError)


def roles_control(roles=None):
    if roles is None:
        roles = ["admin"]

    def roles_permission(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            current_user = get_jwt_identity()
            role = current_user.split(',')[2]
            if role not in roles:
                return error_handler(NoPermission)
            return f(*args, **kwargs)

        return decorated

    return roles_permission

def allcustomer_permission(action="query"):
    # 所有客户权限
    def roles_permission(f):
        @wraps(f)
        def allcustomerdecorated(*args, **kwargs):
            current_user = get_jwt_identity()
            role_id = current_user.split(",")[1]
            print(role_id)
            with app.app_context():
                role_obj = Roles.query.get(role_id)
                perms = role_obj.perms
                perms_list = json.loads(perms)
                ac_action = "allcustomer:" + action
                if ac_action not in perms_list:
                    return error_handler(NoPermission)
            return f(*args, **kwargs)
        return allcustomerdecorated
    return roles_permission


def seacustomer_permission(action="query"):
    # 公海客户权限
    def roles_permission(f):
        @wraps(f)
        def seacustomerdecorated(*args, **kwargs):
            current_user = get_jwt_identity()
            role_id = current_user.split(",")[1]
            print(role_id)
            with app.app_context():
                role_obj = Roles.query.get(role_id)
                perms = role_obj.perms
                perms_list = json.loads(perms)
                ac_action = "seacustomer:" + action
                if ac_action not in perms_list:
                    return error_handler(NoPermission)
            return f(*args, **kwargs)
        return seacustomerdecorated
    return roles_permission



def partner_permission(action="query"):
    # 合作客户权限
    def roles_permission(f):
        @wraps(f)
        def partnerdecorated(*args, **kwargs):
            current_user = get_jwt_identity()
            role_id = current_user.split(",")[1]
            print(role_id)
            with app.app_context():
                role_obj = Roles.query.get(role_id)
                perms = role_obj.perms
                perms_list = json.loads(perms)
                ac_action = "partner:" + action
                if ac_action not in perms_list:
                    return error_handler(NoPermission)
            return f(*args, **kwargs)
        return partnerdecorated
    return roles_permission


def order_permission(action="query"):
    # 合作客户权限
    def roles_permission(f):
        @wraps(f)
        def orderdecorated(*args, **kwargs):
            current_user = get_jwt_identity()
            role_id = current_user.split(",")[1]
            print(role_id)
            with app.app_context():
                role_obj = Roles.query.get(role_id)
                perms = role_obj.perms
                perms_list = json.loads(perms)
                ac_action = "order:" + action
                if ac_action not in perms_list:
                    return error_handler(NoPermission)
            return f(*args, **kwargs)
        return orderdecorated
    return roles_permission

def organ_permission(action="query"):
    # 合作客户权限
    def roles_permission(f):
        @wraps(f)
        def organdecorated(*args, **kwargs):
            current_user = get_jwt_identity()
            role_id = current_user.split(",")[1]
            print(role_id)
            with app.app_context():
                role_obj = Roles.query.get(role_id)
                perms = role_obj.perms
                perms_list = json.loads(perms)
                ac_action = "organ:" + action
                if ac_action not in perms_list:
                    return error_handler(NoPermission)
            return f(*args, **kwargs)
        return organdecorated
    return roles_permission


def get_roles(current_user):
    if current_user:
        user_id = current_user.split(',')[0]
        role_id = current_user.split(',')[1]
        role_name = current_user.split(',')[2]
        dept_id = current_user.split(',')[3]
        return int(user_id), role_id, role_name, dept_id
    else:
        return None
