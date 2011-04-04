# coding: utf-8

from .request import Request

class TradeGetRequest(Request):
    def __init__(self):
        self.fields = None # Trade 的相关字段包括Order
        self.tid = None # 交易单号
        self.method = 'taobao.trade.get'
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

class TradeShippingaddressUpdate(Request):
    def __init__(self):
        self.tid = None
        # optional
        self.receiver_name = None
        self.receiver_mobile = None
        self.receiver_phone = None
        self.receiver_state = None
        self.receiver_city = None
        self.receiver_district = None
        self.receiver_address = None
        self.receiver_zip = None

        self.method = 'taobao.trade.shippingaddress.update'
        self.p = {}

    def set_tid(self, tid):
        self.tid = tid
        self.p['tid'] = tid

    def set_receiver_name(self, rec):
        self.receiver_name = rec
        self.p['receiver_name'] = rec

    def set_receiver_mobile(self, rec):
        self.receiver_mobile = rec
        self.p['receiver_mobile'] = rec

    def set_receiver_phone(self, rec):
        self.receiver_phone = rec
        self.p['receiver_phone'] = rec

    def set_receiver_state(self, rec):
        self.receiver_state = rec
        self.p['receiver_state'] = rec

    def set_receiver_city(self, rec):
        self.receiver_city = rec
        self.p['receiver_city'] = rec

    def set_receiver_district(self, rec):
        self.receiver_district = rec
        self.p['receiver_district'] = rec

    def set_receiver_address(self, rec):
        self.receiver_address = rec
        self.p['receiver_address'] = rec

    def set_receiver_zip(self, rec):
        self.receiver_zip = rec
        self.p['receiver_zip'] = rec
