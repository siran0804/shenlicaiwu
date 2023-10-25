from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db
from shenlibackend.utils.businesstype import *


class Suppliers(BaseModel):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    region = db.Column(db.String(128))
    address = db.Column(db.String(128))

    # 可注册类型
    reg_type = db.Column(db.String(128))

    # 征收方式
    collection_method = db.Column(db.String(128))

    # 政策
    policy = db.Column(db.String(128))

    # 注册+报税+管理费
    reg_tax_mag_fee = db.Column(db.INTEGER)

    # 注销费
    deregistration_fee = db.Column(db.INTEGER)

    # 开票服务费
    invoicing_fee = db.Column(db.String(64))

    # 银行开户费
    bank_account_fee = db.Column(db.INTEGER)

    # 成本
    total_cost = db.Column(db.INTEGER)

    def serialize(self):

        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        data["id"] = str(data["id"])

        def get_dict_value(dictionary, key, default=None):
            return dictionary.get(key, default)

        # 需要转换的键列表
        dict_mapping = {
            "reg_type": REGISTERABLE_TYPE_DICT,
            "collection_method": COLLECTION_METHOD_DICT,
            "policy": POLICY_DICT
            # 添加其他需要转换的键值对和对应的字典
        }

        # 转换指定键的值
        for key, dictionary in dict_mapping.items():
            if key in data:
                data[key + "_name"] = get_dict_value(dictionary, data[key])

        return data

    def __repr__(self):
        return f'<Customer {self.name}>'
