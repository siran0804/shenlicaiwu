# -*- coding: utf-8 -*-

# 你可以按需添加或删除公司类型的名称
COMPANY_TYPE = [
                {"id": '0', "value": "个体工商户"}, {"id": '1', "value": "有限责任公司"},
                {"id": '2', "value": "股份有限公司"}, {"id": '3', "value": "制造公司"}
            ]


CUSTOMER_TYPE = [{"id": '0', "value": "电销"}, {"id": '1', "value": "直客"}]

BUSINESS_TYPE = [{"id": '0', "value": "注册"}, {"id": '1', "value": "个体户开票"}]

INDUSTRY = [{"id": '0', "value": "现代服务"}, {"id": '1', "value": "医疗"}]

CLIENT_PROGRESS = [
                    {"id": '0', "value": "0%"}, {"id": '1', "value": "10%"},
                    {"id": '2', "value": "20%"}, {"id": '3', "value": "30%"},
                    {"id": '4', "value": "40%"}, {"id": '5', "value": "50%"},
                    {"id": '6', "value": "60%"}, {"id": '7', "value": "70%"},
                    {"id": '8', "value": "80%"}, {"id": '9', "value": "90%"},
                    {"id": '10', "value": "100%"},
                   ]

COMPANY_TYPE_DICT = {item["id"]: item["value"] for item in COMPANY_TYPE}
CUSTOMER_TYPE_DICT = {item["id"]: item["value"] for item in CUSTOMER_TYPE}
BUSINESS_TYPE_DICT = {item["id"]: item["value"] for item in BUSINESS_TYPE}
INDUSTRY_DICT = {item["id"]: item["value"] for item in INDUSTRY}
CLIENT_PROGRESS_DICT = {item["id"]: item["value"] for item in CLIENT_PROGRESS}


# 供应商的相应配置
REGISTERABLE_TYPE = [
    {"id": "0", "value": "个体独资企业"}, {"id": "1", "value": "个体工商户"}
]


COLLECTION_METHOD = [
    {"id": "0", "value": "核定征收"}, {"id": "1", "value": "定率征收"}
]


POLICY = [
    {"id": "0", "value": "一般纳税人核定征收"}, {"id": "1", "value": "普票免增值税"}
]

REGISTERABLE_TYPE_DICT = {item["id"]: item["value"] for item in REGISTERABLE_TYPE}


COLLECTION_METHOD_DICT = {item["id"]: item["value"] for item in COLLECTION_METHOD}


POLICY_DICT = {item["id"]: item["value"] for item in POLICY}




if __name__ == '__main__':
    print(COMPANY_TYPE_DICT)
    print(CUSTOMER_TYPE_DICT)
    print(BUSINESS_TYPE_DICT)
    print(INDUSTRY_DICT)
    print(CLIENT_PROGRESS_DICT)
    print(REGISTERABLE_TYPE_DICT)
    print(COLLECTION_METHOD_DICT)
    print(POLICY_DICT)