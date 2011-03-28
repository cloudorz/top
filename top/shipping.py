# coding: utf-8

from .request import Request

class LogisticsTraceSearchRequest(Request):
    def __init__(self):
        self.seller_nick = None
        self.tid = None
        self.method = 'taobao.logistics.trace.search'
        self.p = {}

    def set_seller_nick(self, nick):
        self.seller_nick = nick
        self.p['seller_nick'] = nick

    def set_tid(self, tid):
        self.tid = tid
        self.p['tid'] = tid
