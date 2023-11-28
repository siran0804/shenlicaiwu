from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db


class ServiceProviderContract(BaseModel):
    __tablename__ = "personalperformance"

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
    __tablename__ = "departmentperformance"

    id = db.Column(db.BigInteger, primary_key=True)

    # 公司名称
    company_name = db.Column(db.String(255))

    # 公司负责人id
    company_leaders_id = db.Column(db.BigInteger)

    # 公司负责人姓名
    company_leaders_name = db.Column(db.String(128))

    # 公司负责人联系方式
    company_leaders_contact = db.Column(db.String(128))

    # 团队负责人id
    team_leader_id = db.Column(db.BigInteger)

    # 团队负责人姓名
    team_leader_name = db.Column(db.String(128))

    # 团队负责人联系方式
    team_leader_contact = db.Column(db.String(128))

    # 销售姓名
    sales_name = db.Column(db.String(128))

    # 销售电话
    sales_phone = db.Column(db.String(128))

    # 销售合同 文件或照片上传
    sales_contract = db.Column(db.String(128))
