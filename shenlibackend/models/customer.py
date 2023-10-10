from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db


class Customer(BaseModel):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(50))
    phone = db.Column(db.String(20), unique=True, nullable=False)

    company_type = db.Column(db.String(50))
    customer_type = db.Column(db.String(50))
    business_type = db.Column(db.String(50))
    industry = db.Column(db.String(50))

    client_progress = db.Column(db.String(32))
    sales_consultant = db.Column(db.String(64))

    def __repr__(self):
        return f'<Customer {self.name}>'
