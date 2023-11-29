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

    # 成交价格
    deal_price = db.Column(db.INTEGER)
    # 成交合同
    deal_contract = db.Column(db.String(128))
    # 月份
    month = db.Column(db.INTEGER)
    # 季度
    season = db.Column(db.INTEGER)
    # 年度
    year = db.Column(db.INTEGER)
