# -*- coding: utf-8 -*-

from . import api
from flask import jsonify, request, current_app
from shenlibackend import db
from sqlalchemy import or_, and_, not_, func, desc
from shenlibackend.models.users import User
from shenlibackend.models.users import Roles
from shenlibackend.models.suppliers import Suppliers
from shenlibackend.utils.shenliexceptions import *
from shenlibackend.utils.snowflake import id_generator
from shenlibackend.utils.roleutil import get_roles

from flask_jwt_extended import jwt_required, get_jwt_identity


def error_handler(error):
    response = jsonify({
        'msg': error.msg,
        'code': error.error_code,
        'display': error.display
    })

    return response


# 创建客户
@api.route('/addsupplier', methods=['POST'])
def create_supplier():
    data = request.json
    id = id_generator.generate_id()
    data["id"] = id
    new_supplier = Suppliers(**data)
    try:
        db.session.add(new_supplier)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(SuppliersAddError)

    return jsonify(code=1000, msg="success", display=False)


# 更新客户信息
@api.route('/modifysupplier', methods=['POST'])
def update_supplier():
    data = request.json
    id = data.get("id")
    customer = Suppliers.query.get(id)
    if not customer:
        return error_handler(UserNotExit)

    for key, value in data.items():
        if key != "id":
            if hasattr(customer, key):
                setattr(customer, key, value)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(SuppliersModifyError)
    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


# 删除员工
@api.route('/delsupplier', methods=['POST'])
def delete_supplier():
    data = request.get_json()
    ids = data.get("ids")

    try:
        Suppliers.query.filter(
            Suppliers.id.in_(ids)
        ).delete(synchronize_session=False)

        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(SuppliersDelError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


# 删除员工
@api.route('/querysupplier', methods=['POST'])
# @jwt_required()
def query_supplier():
    data = request.get_json()
    condition = data.get("condition", {})

    # current_user = get_jwt_identity()
    # user_id, role = get_roles(current_user)
    #
    # if role == 'admin':
    #     pass

    page = data.get("page", 1)  # 默认页码为 1
    per_page = data.get("per_page", 10)  # 默认每页显示 10 条记录

    name = condition.get("name", "")

    suppliers_query = Suppliers.query.filter(
        or_(
            Suppliers.name.like("%" + name + "%"),
        )
    )

    # 分页查询
    suppliers = suppliers_query.paginate(page=page, per_page=per_page)

    suppliers_list = [Suppliers.serialize() for Suppliers in suppliers.items]

    return jsonify(
        code=1000,
        msg="success",
        display=False,
        data={
            "data": suppliers_list,
            "total": suppliers.total
        }
    )