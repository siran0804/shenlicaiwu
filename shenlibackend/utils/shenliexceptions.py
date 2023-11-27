# -*- coding: utf-8 -*-
# @Time : 2021/10/20 3:35 下午
# @Author : taonian@nj.iscas.ac.cn
# @File : define_exception.py

from flask import request, json


class ServerError():
    """
    server error
    """
    display = True
    msg = '系统错误！'
    error_code = 5001


# 用户模块异常码
class NoPermission():
    """
    Has no permission
    """
    display = True
    msg = '当前用户角色无权限操作！'
    error_code = 1001


class UserNotExit():
    """
    当前用户不存在
    """
    display = True
    msg = '当前用户不存在'
    error_code = 1002


class PasswordError():
    """
        Has no permission
        """
    display = True
    msg = '密码错误'
    error_code = 1003


class UserAddError():
    """
    Has no permission
    """
    display = True
    msg = '添加用户失败'
    error_code = 1004


class UserModifyError():
    """
    Has no permission
    """
    display = True
    msg = '修改用户失败'
    error_code = 1005


class UserDelError():
    """
    Has no permission
    """
    display = True
    msg = '删除用户失败'
    error_code = 1006


class MissAuthorError():
    """
    未登录
    """
    error_code = 1010
    msg = '未登录'
    display = True


class ResetPwdError():
    """
    未登录
    """
    error_code = 1011
    msg = '重置密码错误'
    display = True


class RoleAddError():
    """
    未登录
    """
    error_code = 1501
    msg = '添加角色失败'
    display = True


class RoleModifyError():
    """
    未登录
    """
    error_code = 1502
    msg = '修改角色失败'
    display = True


class RoleDelError():
    """
    未登录
    """
    error_code = 1502
    msg = '删除角色失败'
    display = True


class DepartmentsAddError():
    """
    multiple login not allowed
    """
    display = True
    msg = "添加部门失败"
    error_code = 2001


class DepartmentsModifyError():
    """
    multiple login not allowed
    """
    display = True
    msg = "修改部门失败"
    error_code = 2002


class DepartmentsDelError():
    """
    multiple login not allowed
    """
    display = True
    msg = "删除部门失败"
    error_code = 2003


class DepartmentsAlterError():
    """
    multiple login not allowed
    """
    display = True
    msg = "移动部门失败"
    error_code = 2004

class DepartmentsNotAllowDelError():
    """
    multiple login not allowed
    """
    display = True
    msg = "根部门不允许删除"
    error_code = 2005


class CustomerAddError():
    display = True
    msg = "新增客户失败"
    error_code = 3001


class CustomerModifyError():
    display = True
    msg = "修改客户失败"
    error_code = 3002


class CustomerDelError():
    display = True
    msg = "删除客户失败"
    error_code = 3003


class CustomerImportError():
    display = True
    msg = "导入客户失败"
    error_code = 3004


class CustomerExportError():
    display = True
    msg = "导出客户失败"
    error_code = 3005


class CustomerQueryError():
    display = True
    msg = "查询客户失败"
    error_code = 3006

class CustomerAssignError():
    display = True
    msg = "分配客户失败"
    error_code = 3007


class SuppliersAddError():
    display = True
    msg = "添加供应商失败"
    error_code = 4001


class SuppliersModifyError():
    display = True
    msg = "修改供应商失败"
    error_code = 4002


class SuppliersDelError():
    display = True
    msg = "删除供应商失败"
    error_code = 4003


class PersonalPerformanceAddError():
    display = True
    msg = "新增个人绩效失败"
    error_code = 5001


class PersonalPerformanceModifyError():
    display = True
    msg = "修改个人绩效失败"
    error_code = 5002


class PersonalPerformanceDelError():
    display = True
    msg = "删除个人绩效失败"
    error_code = 5003






