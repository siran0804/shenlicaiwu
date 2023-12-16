from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db


class ServiceProviderContract(BaseModel):
    __tablename__ = "ServiceProviderContract"

    id = db.Column(db.BigInteger, primary_key=True)

    # 合作地方园区
    cooperation_location = db.Column(db.String(512))

    # 公司名称
    company_name = db.Column(db.String(512))

    # 联系人
    contacts = db.Column(db.String(512))

    # 联系人电话
    contacts_phone = db.Column(db.String(128))

    # 服务商协议
    agreement = db.Column(db.String(128))

    # 直客合同模板
    template = db.Column(db.String(128))


class EmployeeContract(BaseModel):
    __tablename__ = "EmployeeContract"

    id = db.Column(db.BigInteger, primary_key=True)

    # 公司id
    company_id = db.Column(db.BigInteger)

    # 公司负责人id
    company_leaders_id = db.Column(db.BigInteger)

    # 团队负责人id
    team_leader_id = db.Column(db.BigInteger)

    # 销售人员id
    sales_id = db.Column(db.BigInteger)

    # 销售合同 文件或照片上传
    sales_contract = db.Column(db.String(128))
