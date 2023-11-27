from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db


class SealApplication(BaseModel):
    __tablename__ = "personalperformance"

    id = db.Column(db.BigInteger, primary_key=True)

    # 公司名称
    company_name = db.Column(db.String(512))

    # 申请人姓名
    applicant_name = db.Column(db.String(128))

    # 申请人id
    applicant_id = db.Column(db.BigInteger)

    # 申请人联系方式
    applicant_contact = db.Column(db.String(128))

    # 用途说明
    purpose_description = db.Column(db.String(1024))

    # 审批人id
    application_id = db.Column(db.BigInteger)

    # 审批人姓名
    approver_name = db.Column(db.String(255))

    # 审批状态 "待审批"、"已通过"、"已拒绝"
    approval_status = db.Column(db.String(20), default="待审批")

    # 审批意见
    approval_comment = db.Column(db.String(1024))
