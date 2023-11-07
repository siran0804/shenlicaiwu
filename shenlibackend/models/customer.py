from shenlibackend.models.basemodel import BaseModel
from shenlibackend import db
from shenlibackend.utils.businesstype import *

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

    # update progress 更进度 a b c d四个
    update_progress = db.Column(db.String(32), default='d')

    # 是否成交
    is_completed = db.Column(db.BOOLEAN, default=False)

    # 是否是公海客户
    seas = db.Column(db.BOOLEAN, default=False)

    def serialize(self, users_map):

        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        data["id"] = str(data["id"])

        def get_dict_value(dictionary, key, default=None):
            return dictionary.get(key, default)

        # 需要转换的键列表
        dict_mapping = {
            "business_type": BUSINESS_TYPE_DICT,
            "client_progress": CLIENT_PROGRESS_DICT,
            "company_type": COMPANY_TYPE_DICT,
            "customer_type": CUSTOMER_TYPE_DICT,
            "industry": INDUSTRY_DICT,
            # 添加其他需要转换的键值对和对应的字典
        }

        # 转换指定键的值
        for key, dictionary in dict_mapping.items():
            if key in data:
                data[key + "_name"] = get_dict_value(dictionary, data[key])

        if data["sales_consultant"] and users_map:
            user_obj = users_map.get(str(data["sales_consultant"]), None)
            username = user_obj.username if user_obj else None
            data["sales_consultant"] = username

        return data

    def __repr__(self):
        return f'<Customer {self.name}>'


