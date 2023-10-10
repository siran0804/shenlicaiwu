# -*- coding: utf-8 -*-
from . import api
from flask import jsonify, request, current_app
from shenlibackend import db
from shenlibackend.models.users import User
from shenlibackend.models.users import Roles
from shenlibackend.utils.shenliexceptions import *
from shenlibackend.utils.roleutil import get_roles
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity


def error_handler(error):
    response = jsonify({
        'message': error.msg,
        'code': error.error_code,
        'display': error.display
    })

    return response


@api.route('/login', methods=['POST'])
def login():
    request_parameter = request.get_json()

    phone = request_parameter.get("phone", None)
    password = request_parameter.get("password", None)

    user = User.query.filter_by(
        phone=phone
    ).first()

    if not user:
        return error_handler(UserNotExit)

    if user.verify_password(password):

        role_id = user.role
        role_obj = Roles.query.filter_by(
            id=role_id
        ).first()
        role_name = role_obj.name

        identity = str(user.id) + ',' + role_name
        access_token = create_access_token(identity=identity)
        refresh_token = create_refresh_token(identity=identity)
    else:
        return error_handler(PasswordError)

    ret = {
        "code": 1000,
        "msg": "Login Success",
        "display": False,
        "data": {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "role": role_name
        }
    }

    return jsonify(ret)


@api.route("/userinfo", methods=["PODT"])
@jwt_required()
def query_user():
    request_parameter = request.get_json()
    id = request_parameter.get("id", None)

    if not id:
        current_user = get_jwt_identity()
        id, role = get_roles(current_user)

    user = User.query.get(id)
    user_info = user.serialize()
    return jsonify(
        code=1000,
        msg="success",
        display=False,
        data=user_info
    )


@api.route('/addemployee', methods=['POST'])
# @jwt_required()
def add_employee():
    data = request.get_json()
    username = data.get('username')
    phone = data.get('phone')
    id_card_num = data.get('id_card_num')
    email = data.get('email')
    role = data.get('role')
    dept = data.get('dept')

    password = data.get('password', email)

    # 创建用户对象
    user = User(
        username=username,
        phone=phone,
        password=password,
        id_card_num=id_card_num,
        email=email,
        role=role,
        dept=dept
    )

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        return error_handler(UserAddError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


# 修改员工信息
@api.route('/modifyemployee', methods=['POST'])
@jwt_required()
def update_employee():
    data = request.get_json()
    id = data.get("id")
    user = User.query.get(id)

    if not user:
        return error_handler(UserNotExit)

    # 更新员工信息
    user.username = data.get('username', user.username)
    user.phone = data.get('phone', user.phone)
    user.id_card_num = data.get('id_card_num', user.id_card_num)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)
    user.dept = data.get('dept', user.dept)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(UserModifyError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


# 删除员工
@api.route('/delemployee', methods=['POST'])
def delete_employee():
    data = request.get_json()
    ids = data.get("ids")

    try:
        User.query.filter(
            User.id.in_(ids)
        ).delete(synchronize_session=False)

        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(UserDelError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )

@api.route("/hello")
def hello():
    return error_handler(NoPermission)