from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db


class PersonalPerformance(BaseModel):
    __tablename__ = "personalperformance"

    id = db.Column(db.BigInteger, primary_key=True)

    # 公司名称
    company_name = db.Column(db.String(1024))

    customer_name = db.Column(db.String(256))

    contact_phone = db.Column(db.String(128))

    contact_position = db.Column(db.String(128))

    customer_type = db.Column(db.String(128))

    product_type = db.Column(db.String(256))

    sales_consultant_id = db.Column(db.BigInteger)

    sales_consultant_name = db.Column(db.String(256))

    deal_price = db.Column(db.String(128))

    deal_contract = db.Column(db.String(128))

    product_amount = db.Column(db.INTEGER)

    quantity = db.Column(db.INTEGER)

    month = db.Column(db.String(65))


class DepartmentPerformance(BaseModel):
    __tablename__ = "departmentperformance"

    id = db.Column(db.BigInteger, primary_key=True)

    dept = db.Column(db.BigInteger)

    product_type = db.Column(db.String(256))

    product_amount = db.Column(db.INTEGER)

    quantity = db.Column(db.INTEGER)

    month = db.Column(db.DateTime)