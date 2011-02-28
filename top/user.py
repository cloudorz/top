# coding: utf-8

from .request import Request

class UserGetRequest(Request):
    def __init__(self):
        self.fields = None # 查询字段：User数据结构的公开信息字段列表，以半角逗号(,)分隔
        self.nick = None # 用户昵称，多个以半角逗号(,)分隔，最多40个
        self.p = {}

    def set_nick(self, nick):
        self.fields = nick
        self.p['nick'] = nick

    def set_fileds(self, fields):
        self.fields = fields
        self.p['fields'] = fields

    def get_api_method_name(self):
        return 'taobao.user.get'

    def get_api_params(self):
        return self.p

class UsersGetRequest(Request):
    def __init__(self):
        self.fields = None # 查询字段：User数据结构的公开信息字段列表，以半角逗号(,)分隔
        self.nicks = None # 用户昵称，多个以半角逗号(,)分隔，最多40个
        self.p = {}

    def set_nicks(self, nicks):
        self.fields = nicks
        self.p['nicks'] = nicks

    def set_fileds(self, fields):
        self.fields = fields
        self.p['fields'] = fields

    def get_api_method_name(self):
        return 'taobao.users.get'

    def get_api_params(self):
        return self.p
