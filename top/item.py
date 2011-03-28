# coding: utf-8

from .request import Request

class ItemGetRequest(Request):
    def __init__(self):
        self.fields = None # 为商品提供的所选字段详情见top
        self.nick = None # 可选
        self.num_iid = None # 商品数字id
        self.method = 'taobao.item.get'
        self.p = {}

    def set_fields(self, fields):
        self.fields = fields
        self.p['fields'] = fields

    def set_nick(self, nick):
        self.nick = nick
        self.p['nick'] = nick

    def set_num_iid(self, num_iid):
        self.num_iid = num_iid
        self.p['num_iid'] = num_iid
