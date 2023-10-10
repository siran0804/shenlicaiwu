# -*- coding: utf-8 -*-

from . import api
from flask import jsonify, request, current_app
from shenlibackend import db
from sqlalchemy import or_, and_, not_, func, desc
from shenlibackend.models.users import User
from shenlibackend.models.users import Roles
from shenlibackend.models.customer import Customer
from shenlibackend.utils.shenliexceptions import *
from shenlibackend.utils.snowflake import id_generator
from shenlibackend.utils.roleutil import get_roles

from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity



def error_handler(error):
    response = jsonify({
        'message': error.msg,
        'code': error.error_code,
        'display': error.display
    })

    return response


# 创建客户
@api.route('/addcustomer', methods=['POST'])
def create_customer():
    data = request.json
    id = id_generator.generate_id()
    data["id"] = id
    new_customer = Customer(**data)
    try:
        db.session.add(new_customer)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(CustomerAddError)

    return jsonify(code=1000, msg="success", display=False)


# 更新客户信息
@api.route('/modifycustomer', methods=['POST'])
def update_customer():
    data = request.json
    id = data.get("id")
    customer = Customer.query.get(id)
    if not customer:
        return error_handler(UserNotExit)

    for key, value in data.items():
        if key != "id":
            setattr(customer, key, value)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(CustomerModifyError)
    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


# 删除员工
@api.route('/delcustomer', methods=['POST'])
def delete_customer():
    data = request.get_json()
    ids = data.get("ids")

    try:
        Customer.query.filter(
            Customer.id.in_(ids)
        ).delete(synchronize_session=False)

        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(CustomerDelError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


# 删除员工
@api.route('/querycustomer', methods=['POST'])
@jwt_required()
def query_customer():
    data = request.get_json()
    condition = data.get("condition")

    current_user = get_jwt_identity()
    user_id, role = get_roles(current_user)

    if role == 'admin':
        pass

    page = data.get("page", 1)  # 默认页码为 1
    per_page = data.get("per_page", 10)  # 默认每页显示 10 条记录

    customer_query = Customer.query.filter(
        or_(
            Customer.name.like("%" + condition + "%"),
            Customer.phone.like("%" + condition + "%"),
            Customer.sales_consultant.like("%" + condition + "%")
        )
    )

    # 分页查询
    customers = customer_query.paginate(page=page, per_page=per_page)

    customer_list = [customer.serialize() for customer in customers.items]

    return jsonify(
        code=1000,
        msg="success",
        display=False,
        data={
            "data": customer_list,
            "total": customers.total
        }
    )