
from shenlibackend import db
from shenlibackend.models.departments import Departments
from shenlibackend.models.users import User, Roles


class UserDao(object):
    """
    用户查询
    """

    @classmethod
    def get_company_leader(cls, dept=None):
        roles = RoleDao.get_role_by_name(name='company_leader')
        roles_ids = [item.id for item in roles]

        if not dept:
            leaders = User.query.filter(
                User.role.in_(roles_ids)
            ).all()
        else:


            leaders = User.query.filter(
                User.dept == dept,
                User.role.in_(roles_ids)
            ).all()

        return leaders

    @classmethod
    def get_team_leader(cls, dept=None):
        roles = RoleDao.get_role_by_name(name='team_leader')
        roles_ids = [item.id for item in roles]

        if not dept:
            leaders = User.query.filter(
                User.role.in_(roles_ids)
            ).all()
        else:
            dept = DepartmentDao.get_department_by_id(dept)
            idlink = dept.idlink
            dept_ids = idlink.split("|")
            if len(dept_ids) == 1:
                return []
            else:
                dept_id = dept_ids[1]
                leaders = User.query.filter(
                    User.dept == dept_id,
                    User.role.in_(roles_ids)
                ).all()

        return leaders

    @classmethod
    def get_up_leaders(cls, dept):
        dept_obj = DepartmentDao.get_department_by_id(dept)
        idlink = dept_obj.idlink
        idlink_split = idlink.split('|')
        if len(idlink_split) == 1:
            return jsonify(code=1000, msg="success", data=[])

        up_dept_id = idlink_split[-2]

        role_objs = Roles.query.filter(
            Roles.name.in_(['team_leader', 'company_leader', 'ceo'])
        ).all()

        roles_ids = [item.id for item in role_objs]

        leaders = User.query.filter(
            User.dept == up_dept_id,
            User.role.in_(roles_ids)
        ).all()

        return leaders

    @classmethod
    def ceo(cls):
        roles = RoleDao.get_role_by_name("ceo")
        roles_ids = [item.id for item in roles]

        ceo = User.query.filter(
            User.role.in_(roles_ids)
        ).all()

        return ceo


class DepartmentDao(object):
    """
    部门查询
    """
    @classmethod
    def get_department_by_id(cls, id):
        dept = Departments.query.filter(
            Departments.id == id
        ).first()

        return dept



class RoleDao(object):
    """
    角色查询
    """
    @classmethod
    def get_role_by_name(cls, name):
        roles = Roles.query.filter(
            Roles.name == name
        ).all()

        return roles

    @classmethod
    def get_roles_by_names(cls, names):
        roles = Roles.query.filter(
            Roles.name.in_(names)
        ).all()

        return roles



