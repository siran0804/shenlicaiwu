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
    
    reg_tax_mag_fee = db.Column(db.INTEGER)

    deregistration_fee = db.Column(db.INTEGER)

    invoicing_fee = db.Column(db.INTEGER)

    bank_account_fee = db.Column(db.INTEGER)

    total_cost = db.Column(db.INTEGER)

    def __repr__(self):
        return f'<Customer {self.name}>'
