from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db


class Customer(BaseModel):
    id = db.Column(db.BigInteger, primary_key=True)

    # 客户名称
    name = db.Column(db.String(255), nullable=False)

    # 联系人
    contact = db.Column(db.String(50))

    # 联系电话
    phone = db.Column(db.String(20), unique=True, nullable=False)

    # 公司类型
    company_type = db.Column(db.INTEGER)

    # 客户类型
    customer_type = db.Column(db.INTEGER)

    # 业务类型
    business_type = db.Column(db.INTEGER)

    # 行业
    industry = db.Column(db.INTEGER)

    # 客户进度
    client_progress = db.Column(db.INTEGER)

    # 销售顾问
    sales_consultant = db.Column(db.BigInteger)




    def __repr__(self):
        return f'<Customer {self.name}>'
