# -*- coding: utf-8 -*-

from . import api
from flask import jsonify, request, current_app
from shenlibackend import db

from shenlibackend.models.contract import *
from shenlibackend.utils.snowflake import id_generator

from shenlibackend.utils.shenliexceptions import *


def error_handler(error):
    response = jsonify({
        'msg': error.msg,
        'code': error.error_code,
        'display': error.display
    })

    return response


@api.route('/addspcontract', methods=['POST'])
def create_spcontract():
    data = request.json
    id = id_generator.generate_id()
    data["id"] = id
    new_spc = ServiceProviderContract(**data)
    try:
        db.session.add(new_spc)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(ServiceProviderContractAddError)

    return jsonify(code=1000, msg="success", display=False)


@api.route('/modifyspcontract', methods=['POST'])
def update_spcontract():
    data = request.json
    id = data.get("id")
    self_spc = ServiceProviderContract.query.get(id)
    if not self_spc:
        return error_handler(UserNotExit)

    for key, value in data.items():
        if key != "id":
            if hasattr(self_spc, key):
                setattr(self_spc, key, value)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(ServiceProviderContractModifyError)
    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


@api.route('/delspcontract', methods=['POST'])
def delete_spcontract():
    data = request.get_json()
    ids = data.get("ids")

    try:
        ServiceProviderContract.query.filter(
            ServiceProviderContract.id.in_(ids)
        ).delete(synchronize_session=False)

        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(ServiceProviderContractDelError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


@api.route('/addecontract', methods=['POST'])
def create_econtract():
    data = request.json
    id = id_generator.generate_id()
    data["id"] = id
    new_spc = EmployeeContract(**data)
    try:
        db.session.add(new_spc)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(EmployeeContractAddError)

    return jsonify(code=1000, msg="success", display=False)


@api.route('/modifyecontract', methods=['POST'])
def update_econtract():
    data = request.json
    id = data.get("id")
    self_spc = EmployeeContract.query.get(id)
    if not self_spc:
        return error_handler(UserNotExit)

    for key, value in data.items():
        if key != "id":
            if hasattr(self_spc, key):
                setattr(self_spc, key, value)
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(EmployeeContractModifyError)
    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


@api.route('/delecontract', methods=['POST'])
def delete_econtract():
    data = request.get_json()
    ids = data.get("ids")

    try:
        EmployeeContract.query.filter(
            EmployeeContract.id.in_(ids)
        ).delete(synchronize_session=False)

        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(EmployeeContractDelError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


















































