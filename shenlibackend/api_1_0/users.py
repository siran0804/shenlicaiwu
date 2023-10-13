# -*- coding: utf-8 -*-
from . import api
from flask import jsonify, request, current_app
from sqlalchemy import or_
from shenlibackend import db
from shenlibackend.models.users import User
from shenlibackend.models.users import Roles
from shenlibackend.models.departments import Departments
from shenlibackend.utils.shenliexceptions import *
from shenlibackend.utils.roleutil import get_roles
from shenlibackend.utils.snowflake import id_generator
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

    id = id_generator.generate_id()
    # 创建用户对象
    user = User(
        id=id,
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
        current_app.logger.error(str(e))
        return error_handler(UserAddError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


# 修改员工信息
@api.route('/modifyemployee', methods=['POST'])
# @jwt_required()
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


@api.route("/queryemployee", methods=["POST"])
# @jwt_required()
def query_employee():
    data = request.get_json()
    condition = data.get("condition", "")
    page = data.get("page", 1)
    per_page = data.get("per_page", 10)

    employee_query = User.query.filter(
        or_(
            User.username.like("%" + condition + "%"),
            User.phone.like("%" + condition + "%"),
            User.email.like("%" + condition + "%")
        )
    )

    employee = employee_query.paginate(page=page, per_page=per_page)
    employee_list = [emp.serialize() for emp in employee.items]

    departments = Departments.query.all()
    departments_map = {
        dept.id: dept for dept in departments
    }

    roles = Roles.query.all()
    roles_map = {
        role.id: role for role in roles
    }

    for emp in employee_list:
        dept = departments_map.get(emp["dept"], None)
        deptname = dept.name if dept else ""

        role = roles_map.get(emp["role"], None)
        role_dispname = role.dispname if role else ""

        emp["deptname"] = deptname
        emp["role_dispname"] = role_dispname

        emp["dept"] = str(emp["dept"])
        emp["role"] = str(emp["role"])

    return jsonify(
        code=1000,
        msg="success",
        display=False,
        data={
            "data": employee_list,
            "total": employee.total
        }
    )


@api.route("/resetpwd", methods=["POST"])
# @jwt_required()
def reset_pwd():
    data = request.get_json()
    id = data.get("id")
    employee = User.query.get(id)
    employee.password = employee.email
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(ResetPwdError)
    return jsonify(code=1000, msg="success", display=False)


@api.route("/queryrole", methods=["POST"])
def query_role():
    data = request.get_json()
    condition = data.get("condition", "")
    page = data.get("page", 1)
    per_page = data.get("per_page", 999)

    role_query = Roles.query.filter(
        Roles.dispname.like("%" + condition + "%")
    )
    role_objs = role_query.paginate(page, per_page)
    role_list = [role_obj.serialize() for role_obj in role_objs.items]
    return jsonify(code=1000, msg="success", data={
        "data": role_list,
        "total": role_objs.total
    })


@api.route("/addrole", methods=["POST"])
def add_role():
    data = request.get_json()
    name = data.get('roleAuth')
    dispname = data.get('roleName')
    permission = data.get("permission")

    id = id_generator.generate_id()
    # 创建用户对象
    role = Roles(
        id=id,
        name=name,
        dispname=dispname,
        permission=permission
    )

    try:
        db.session.add(role)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(RoleAddError)
    return jsonify(code=1000, msg="success", display=False)


@api.route('/modifyuser', methods=['POST'])
# @jwt_required()
def modify_user():
    data = request.get_json()
    id = data.get("id")
    role = Roles.query.get(id)

    # 更新员工信息
    role.name = data.get('username', role.name)
    role.dispname = data.get('dispname', role.dispname)

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(RoleModifyError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


@api.route('/delrole', methods=['POST'])
def del_role():
    data = request.get_json()
    ids = data.get("ids")

    try:
        Roles.query.filter(
            Roles.id.in_(ids)
        ).delete(synchronize_session=False)

        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(RoleDelError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


@api.route("/hello")
def hello():
    return error_handler(NoPermission)