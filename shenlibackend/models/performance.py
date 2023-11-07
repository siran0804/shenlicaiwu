from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db


class PersonalPerformance(BaseModel):
    __tablename__ = "personalperformance"

    id = db.Column(db.BigInteger, primary_key=True)

    employee = db.Column(db.BigInteger)

    employee_name = db.Column(db.String(256))

    product_type = db.Column(db.String(256))

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