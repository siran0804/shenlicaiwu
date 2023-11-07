from . import api
from flask import jsonify, request, current_app
from shenlibackend import db

from shenlibackend.models.performance import PersonalPerformance, DepartmentPerformance
from shenlibackend.utils.snowflake import id_generator

from shenlibackend.utils.shenliexceptions import *


def error_handler(error):
    response = jsonify({
        'msg': error.msg,
        'code': error.error_code,
        'display': error.display
    })

    return response


# 创建客户
@api.route('/addselfperformance', methods=['POST'])
def create_supplier():
    data = request.json
    id = id_generator.generate_id()
    data["id"] = id
    new_selfperformance = PersonalPerformance(**data)
    try:
        db.session.add(new_selfperformance)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(PersonalPerformanceAddError)

    return jsonify(code=1000, msg="success", display=False)


# 更新客户信息
@api.route('/modifyselfperformance', methods=['POST'])
def update_supplier():
    data = request.json
    id = data.get("id")
    self_performance = PersonalPerformance.query.get(id)
    if not self_performance:
        return error_handler(UserNotExit)

    for key, value in data.items():
        if key != "id":
            if hasattr(self_performance, key):
                setattr(self_performance, key, value)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(PersonalPerformanceModifyError)
    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


# 删除员工
@api.route('/delselfperformance', methods=['POST'])
def delete_supplier():
    data = request.get_json()
    ids = data.get("ids")

    try:
        PersonalPerformance.query.filter(
            PersonalPerformance.id.in_(ids)
        ).delete(synchronize_session=False)

        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(PersonalPerformanceDelError)

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

    self_performance_query = PersonalPerformance.query

    if condition:
        name = condition.get("employee_name", "")

        if name:
            self_performance_query = self_performance_query.filter(
                PersonalPerformance.name.like("%" + name + "%")
            )

    # 分页查询
    self_performances = self_performance_query.paginate(page=page, per_page=per_page)

    self_performances_list = [self_performance.serialize() for self_performance in self_performances.items]

    return jsonify(
        code=1000,
        msg="success",
        display=False,
        data={
            "data": self_performances_list,
            "total": self_performances.total
        }
    )