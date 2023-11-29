from . import api
from flask import jsonify, request, current_app
from sqlalchemy import func

from shenlibackend import db


from shenlibackend.models.performance import PersonalPerformance, DepartmentPerformance
from shenlibackend.utils.snowflake import id_generator

from shenlibackend.utils.shenliexceptions import *

from datetime import datetime
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from shenlibackend.utils.deptsutil import RolesHelper, DeptmentHelper

def error_handler(error):
    response = jsonify({
        'msg': error.msg,
        'code': error.error_code,
        'display': error.display
    })

    return response


# 创建客户
@api.route('/addselfperformance', methods=['POST'])
def create_selfperformance():
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
def update_selfperformance():
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
def delete_selfperformance():
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


@api.route("/queryselfperformance", methods=['POST'])
@jwt_required
def query_selfperformance():

    data = request.get_json()

    role_helper = RolesHelper()
    user_id = role_helper.user_id

    condition = data.get("condition", {})

    page = data.get("page", 1)  # 默认页码为 1
    per_page = data.get("per_page", 10)  # 默认每页显示 10 条记录

    current_time = datetime.now()
    current_year = current_time.year
    current_month = current_time.month
    current_quarter = (current_month - 1) // 3 + 1

    year = data.get("year", None)
    season = data.get("season", None)
    month = data.get("year", None)

    year_total, season_total, month_total = None, None, None

    if not year:
        year = current_year
        season = current_quarter
        month = current_month

    performance_query = PersonalPerformance.query.filter(
        PersonalPerformance.sales_consultant_id == user_id,
    )

    performance_query = performance_query.filter(
        PersonalPerformance.year == year,
    )

    year_total = performance_query.with_entities(func.sum(PersonalPerformance.deal_price)).scalar()

    if season:
        performance_query = performance_query.filter(
            PersonalPerformance.season == season
        )

        season_total = performance_query.with_entities(func.sum(PersonalPerformance.deal_price)).scalar()

    if month:
        performance_query = performance_query.filter(
            PersonalPerformance.month == month
        )

        month_total = performance_query.with_entities(func.sum(PersonalPerformance.deal_price)).scalar()


    if condition:
        employee_name = condition.get("employee_name", "")
        product_type = condition.get("product_type", "")

        if employee_name:
            performance_query = performance_query.filter(
                PersonalPerformance.employee_name.like("%" + employee_name + "%")
            )

        if product_type:
            performance_query = performance_query.filter(
                PersonalPerformance.product_type == product_type
            )


    # 分页查询
    performance = performance_query.paginate(page=page, per_page=per_page)

    performance_list = [p.serialize() for p in performance.items]

    return jsonify(
        code=1000,
        msg="success",
        display=False,
        data={
            "data": performance_list,
            "total": performance.total,
            "year_total": year_total,
            "season_total": season_total,
            "month_total": month_total
        }
    )
