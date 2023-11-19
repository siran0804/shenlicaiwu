# -*- coding: utf-8 -*-

from shenlibackend.models.departments import Departments
from shenlibackend.models.users import User
from shenlibackend.utils.roleutil import get_roles
from flask_jwt_extended import get_jwt_identity


class DeptmentHelper():
    def __init__(self, dept_id, idlink):
        self.dept_id = dept_id
        self.idlink = idlink

    def get_sub_dept_obj(self):
        all_dept_objs = Departments.query.filter(
            Departments.idlink.startswith(self.idlink)
        ).all()

        return all_dept_objs


class RolesHelper():
    def __init__(self):
        current_user = get_jwt_identity()
        user_id, role_id, role_name, dept_id = get_roles(current_user)
        self.user_id = user_id
        self.role_id = role_id
        self.role_name = role_name
        self.dept_id = dept_id

    def is_manager(self):
        if self.role_name == 'manager':
            return True
        return False

    def is_admin(self):
        if self.role_name == 'admin':
            return True
        return False

    def is_general(self):
        if self.role_name == 'general':
            return True
        return False










