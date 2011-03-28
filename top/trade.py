# coding: utf-8

from .request import Request

class TradeGetRequest(Request):
    def __init__(self):
        self.fields = None # Trade 的相关字段包括Order
        self.tid = None # 交易单号
        self.method = 'taobao.trade.get'
        self.data_path = '_'.join(self.method.split('.')[1:]+['response'])
        self.p = {}

    def set_fields(self, fields):
        self.fields = fields
        self.p['fields'] = fields

    def set_tid(self, tid):
        self.tid = tid
        self.p['tid'] = tid

class TradesBoughtGetRequest(Request):
    def __init__(self):
        self.fields = None
        # 以下为可选
        self.start_created = None 
        self.end_created = None
        self.status = None
        self.seller_nick = None
        self.type = None
        self.page_no = None
        self.page_size = None
        self.rate_status = None

        self.method = 'taobao.trades.bought.get'
        self.p = {}

    def set_fields(self, fields):
        self.fields = fields
        self.p['fields'] = fields

    def set_start_created(self, st):
        self.start_created = st
        self.p['start_created'] = st

    def set_end_created(self, et):
        self.end_created = et
        self.p['end_created'] = et

    def set_status(self, status):
        self.status = status
        self.p['status'] = status

    def set_seller_nick(self, seller):
        self.seller_nick = seller
        self.p['seller_nick'] = seller

    def set_type(self, tt):
        self.type = tt
        self.p['type'] = tt

    def set_page_no(self, no):
        self.page_no = no
        self.p['page_no'] = no

    def set_page_size(self, size):
        self.page_size = size
        self.p['page_size'] = size
    
    def set_rate_status(self, rs):
        self.rate_status = rs
        self.p['rate_status'] = rs
