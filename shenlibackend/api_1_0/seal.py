
# -*- coding: utf-8 -*-

from . import api
from flask import jsonify, request, current_app
from shenlibackend import db

from shenlibackend.models.seal import *
from shenlibackend.models.departments import Departments
from shenlibackend.utils.snowflake import id_generator

from shenlibackend.utils.shenliexceptions import *
from shenlibackend.utils.deptsutil import RolesHelper



def error_handler(error):
    response = jsonify({
        'msg': error.msg,
        'code': error.error_code,
        'display': error.display
    })

    return response


@api.route('/addsealapplication', methods=['POST'])
def create_sealapplication():
    data = request.json
    id = id_generator.generate_id()
    data["id"] = id
    new_spc = SealApplication(**data)
    try:
        db.session.add(new_spc)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(SealApplicationAddError)

    return jsonify(code=1000, msg="success", display=False)


@api.route('/modifysealapplication', methods=['POST'])
def update_sealapplication():
    data = request.json
    id = data.get("id")
    self_spc = SealApplication.query.get(id)
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
        return error_handler(SealApplicationModifyError)
    return jsonify(
        code=1000,
        msg="success",
        display=False
    )


@api.route('/delsealapplication', methods=['POST'])
def delete_sealapplication():
    data = request.get_json()
    ids = data.get("ids")

    try:
        SealApplication.query.filter(
            SealApplication.id.in_(ids)
        ).delete(synchronize_session=False)

        db.session.commit()
    except Exception as e:
        current_app.logger.error(str(e))
        return error_handler(SealApplicationDelError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )

# 审批接口
@api.route("/approvalsealapplication", methods=["POST"])
def approval_sealapplication():
    data = request.json
    id = data.get("id")
    approval_result = data.get("approval_result", "")
    next_approver_id = data.get("next_approver_id", None)
    next_approver_name = data.get("next_approver_name", None)

    rh = RolesHelper()
    self_spc = SealApplication.query.get(id)

    if str(self_spc.applicant_id) != str(rh.user_id):
        return error_handler(NoPermission)

    if approval_result:
        if approval_result == "同意":
            if str(rh.user_id) == str(current_app.config["ADMIN_ID"]):
                self_spc.approval_status = "已通过"
            else:
                self_spc.application_id = next_approver_id
                self_spc.approver_name = next_approver_name
        if approval_result == "不同意":
            self_spc.approval_status = "已拒绝"

        try:
            db.session.commit()
        except Exception as e:
            current_app.logger.error(str(e))
            return error_handler(SealApplicationApprovalError)

    return jsonify(
        code=1000,
        msg="success",
        display=False
    )




















