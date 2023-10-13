# -*- coding: utf-8 -*-

from . import api
from flask import jsonify, current_app

# 你可以按需添加或删除公司类型的名称
COMPANY_TYPE = [
                "个体工商户", "有限责任公司", "股份有限公司", "合伙企业", "有限合伙公司",
                "股份公司", "社会企业", "非营利组织", "合作社", "科技初创公司", "制造公司",
                "金融机构", "餐饮业", "媒体和娱乐公司", "教育机构"
            ]

CUSTOMER_TYPE = [{"id": 0, "value": "电销"}, {"id": 1, "value": "直客"}]

BUSINESS_TYPE = [{"id": 0, "value": "注册"}, {"id": 1, "value": "个体户开票"}]

INDUSTRY = [{"id": 0, "value": "现代服务"}, {"id": 1, "value": "医疗"}]

CLIENT_PROGRESS = [
    "0%", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"
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
