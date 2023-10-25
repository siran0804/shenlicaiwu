# -*- coding: utf-8 -*-

from . import api
from flask import jsonify, current_app

from shenlibackend.utils.businesstype import *


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


@api.route('/registerabletype', methods=['POST'])
def registerable_type():

    return jsonify(
        code=1000,
        msg="success",
        data=REGISTERABLE_TYPE
    )


@api.route('/collectionmethod', methods=['POST'])
def collection_method():

    return jsonify(
        code=1000,
        msg="success",
        data=COLLECTION_METHOD
    )


@api.route('/policy', methods=['POST'])
def policy():

    return jsonify(
        code=1000,
        msg="success",
        data=POLICY
    )
