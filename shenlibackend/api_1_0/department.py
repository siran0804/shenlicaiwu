# -*- coding: utf-8 -*-
from . import api
from flask_jwt_extended import jwt_required
from flask import jsonify, request, current_app
from shenlibackend import db
from shenlibackend.models.users import User
from shenlibackend.models.departments import Departments
from shenlibackend.utils.shenliexceptions import *
from shenlibackend.utils.snowflake import id_generator
from shenlibackend.utils import roleutil


def error_handler(error):
    response = jsonify({
        'message': error.msg,
        'code': error.error_code,
        'display': error.display
    })

    return response


@api.route("/adddept", methods=["POST"])
# @jwt_required()
def add_departments():

    request_param = request.get_json()
    name = request_param.get("name", '')
    parent = request_param.get("parent", None)
    pname = request_param.get("pname", None)

    parent_obj = Departments.query.filter_by(id=parent).first()
    id = id_generator.generate_id()
    idlink = parent_obj.idlink + "|" + str(id)
    dept_obj = Departments(id=id, name=name, idlink=idlink, parent=parent, pname=pname)

    try:
        db.session.add(dept_obj)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(str(e))
        return error_handler(DepartmentsAddError)

    return jsonify(code=1000, msg="success", display=False)


@api.route("/querydept", methods=["POST"])
# @jwt_required()
def query_depts():
    request_param = request.get_json()
    id = request_param.get("id", None)
    if not id:
        # 获取根部门
        dept = current_app.config.get("RDEPT")
        id = dept
        dept_obj = Departments.query.filter_by(id=id).first()
        data = [{"id": str(dept_obj.id), "name": dept_obj.name,
                 "parent": dept_obj.parent, "pname": dept_obj.pname,
                 "idlink": dept_obj.idlink, "children": []}]
        total = [1]
        get_depts(data, total)
        return jsonify(code=1000, msg="success", data=data, display=False)


@api.route("/modifydept", methods=["POST"])
def modify_dept():
    request_param = request.get_json()
    id = request_param.get("id", None)
    name = request_param.get("name", '')
    dept_obj = Departments.query.filter_by(id=id).first()
    dept_obj.name = name
    try:
        db.session.commit()
        return jsonify(code=1000, msg="success", display=False)
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(DepartmentsModifyError)


@api.route("/deldept", methods=["POST"])
def del_dept():
    request_param = request.get_json()
    id = request_param.get("id", None)
    dept_obj = Departments.query.filter_by(id=id).first()

    dept_idlink = dept_obj.idlink
    all_dept = Departments.query.filter(Departments.idlink.startswith(dept_idlink)).all()
    all_dept_id = [item.id for item in all_dept]

    try:
        t = User.query.filter(
            User.dept.in_(all_dept_id)
        ).count()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(DepartmentsDelError)

    if t and t > 0:
        return jsonify(code=6061, msg="该部门或子部门下存在员工，不允许删除", display=True)

    try:
        db.session.delete(dept_obj)
        db.session.commit()
        return jsonify(code=1000, msg="success", display=False)
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(str(e))
        return error_handler(DepartmentsDelError)


@api.route("/alterdepts", methods=["POST"])
@jwt_required()
def alter_structure():
    request_param = request.get_json()
    id = request_param.get("id", None)
    parent = request_param.get("parent", None)
    childrens = []
    get_children(id, childrens)

    parent_obj = Departments.query.filter_by(id=parent).first()
    dept_obj = Departments.query.filter_by(id=id).first()
    dept_obj.parent = parent
    dept_obj.idlink = parent_obj.idlink + "|" + str(id)

    if len(childrens) != 0:
        for item in childrens:
            item_obj = Departments.query.filter_by(id=item).first()
            index = item_obj.idlink.find(str(id))
            temp_idlink = parent_obj.idlink + "|" + item_obj.idlink[index:]
            item_obj.idlink = temp_idlink

    try:
        db.session.commit()
        return jsonify(code=1000, msg="success", display=False)
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(DepartmentsAlterError)


def get_depts(data, total):
    for d in data:
        depts = Departments.query.filter_by(parent=d["id"]).all()
        total[0] += len(depts)
        if len(depts) != 0:
            for dept in depts:
                d["children"].append({"id": str(dept.id), "name": dept.name,
                                      "parent": str(dept.parent), "pname": dept.pname,
                                      "idlink": dept.idlink, "children": []})
            get_depts(d["children"], total)


def get_children(parent, childrens):
    depts_obj = Departments.query.filter_by(parent=parent).all()
    if len(depts_obj) != 0:
        for dept_obj in depts_obj:
            childrens.append(str(dept_obj.id))
            get_children(str(dept_obj.id), childrens)