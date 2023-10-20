from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db


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

    def __repr__(self):
        return f'<Customer {self.name}>'
