# coding: utf-8

from .request import Request

class SubscribeGetRequest(Request):
    def __init__(self):
        self.lease_id = None
        self.nick = None
        self.method = 'taobao.appstore.subscribe.get'
        self.p = {}

    def set_lease_id(self, lease_id):
        self.lease_id = lease_id
        self.p['lease_id'] = lease_id

    def set_nick(self, nick):
        self.nick = nick
        self.p['nick'] = nick
