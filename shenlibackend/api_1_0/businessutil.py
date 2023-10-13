# -*- coding: utf-8 -*-

from . import api
from flask import jsonify, current_app

# 你可以按需添加或删除公司类型的名称
COMPANY_TYPE = [
                {"id": 0, "value": "个体工商户"}, {"id": 1, "value": "有限责任公司"},
                {"id": 2, "value": "股份有限公司"}, {"id": 3, "value": "制造公司"}
            ]


CUSTOMER_TYPE = [{"id": 0, "value": "电销"}, {"id": 1, "value": "直客"}]

BUSINESS_TYPE = [{"id": 0, "value": "注册"}, {"id": 1, "value": "个体户开票"}]

INDUSTRY = [{"id": 0, "value": "现代服务"}, {"id": 1, "value": "医疗"}]

CLIENT_PROGRESS = [
                    {"id": 0, "value": "0%"}, {"id": 1, "value": "10%"},
                    {"id": 2, "value": "20%"}, {"id": 3, "value": "30%"},
                    {"id": 4, "value": "40%"}, {"id": 5, "value": "50%"},
                    {"id": 6, "value": "60%"}, {"id": 7, "value": "70%"},
                    {"id": 8, "value": "80%"}, {"id": 9, "value": "90%"},
                    {"id": 10, "value": "100%"},
                   ]


@api.route('/businesstype', methods=['POST'])
def business_type():

    return jsonify(
        code=1000,
        msg="success",
        data=BUSINESS_TYPE
    )


@api.route('/industry', methods=['POST'])
def industry():

    return jsonify(
        code=1000,
        msg="success",
        data=INDUSTRY
    )


@api.route('/clientprogress', methods=['POST'])
def client_progress():

    return jsonify(
        code=1000,
        msg="success",
        data=CLIENT_PROGRESS
    )


@api.route('/companytype', methods=['POST'])
def company_type():

    return jsonify(
        code=1000,
        msg="success",
        data=COMPANY_TYPE
    )


@api.route('/customertype', methods=['POST'])
def customer_type():

    return jsonify(
        code=1000,
        msg="success",
        data=CUSTOMER_TYPE
    )
