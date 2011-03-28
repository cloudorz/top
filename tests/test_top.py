# coding: utf-8

import sys, unittest, pprint, datetime

sys.path.append('/Users/cloud/mywork/webdev/top')
from top import *

c = TopClient(key='12225810', secret='f8f8eff13f26d2882d9da483ccc0f36e')
session_key = '239001c5ccb90dfd1b65e915fa7e4597448b8'
pp = pprint.PrettyPrinter(indent=4)

class TestTopRequest(unittest.TestCase):
    def test_user_get(self):
        ''' UserGetRequest can get right data?
        '''
        r = UserGetRequest()
        r.set_nick('mydewdew')
        r.set_fields('user_id,nick,location,udi,sex')

        rsp = c.execute(r)
        self.assertTrue(rsp and 'user' in rsp and rsp['user'] and 'nick' in rsp['user'] \
                and rsp['user']['nick'] == 'mydewdew')

    def test_users_get(self):
        ''' UsersGetRequest can get right data?
        '''
        r = UsersGetRequest()
        r.set_nicks('mydewdew,84607362qq')
        r.set_fields('user_id,nick,location')
        rsp = c.execute(r)
        self.assertTrue(rsp and 'users' in rsp and 'user' in rsp['users'] and len(rsp['users']['user'])==2)

    def test_subscribe_get(self):
        ''' SubscribeGetRequest can get right data?
        '''
        r = SubscribeGetRequest()
        r.set_nick('mydewdew')

        rsp = c.execute(r)
        self.assertTrue(rsp and 'user_subscribe' in rsp and 'status' in rsp['user_subscribe'])

    def test_shipping_trace_search(self):
        ''' LogisticsTraceSearchRequest can search right data?
        '''
        r = LogisticsTraceSearchRequest()
        r.set_seller_nick(u'展宇数码专营店')
        r.set_tid('66896518620063')

        rsp = c.execute(r)
        self.assertTrue(rsp)

    def test_item_get(self):
        ''' ItemGetRequest can get the id's item?
        '''
        r = ItemGetRequest()
        r.set_fields('iid,detail_url,num_iid,nick,item_imgs,location,prop_imgs.url,second_kill')
        r.set_nick(u'展宇数码专营店')
        r.set_num_iid('7669995999')

        rsp = c.execute(r)
        self.assertTrue(rsp)

    def test_trade_get(self):
        ''' TradeGetRequest can get the trade and orders by tid
        '''
        r = TradeGetRequest()
        r.set_fields('seller_nick, buyer_nick, title, type, created, tid, seller_rate, buyer_rate, status,\
                payment, discount_fee, adjust_fee, post_fee, total_fee, pay_time, end_time, modified,\
                consign_time, buyer_obtain_point_fee, point_fee, real_point_fee, received_payment, commission_fee,\
                buyer_memo, seller_memo, alipay_no, buyer_message, pic_path, num_iid, num, price, cod_fee,\
                cod_status, shipping_type,orders.iid,orders.pic_path,orders.num_iid')
        r.set_tid('60400293320099')

        rsp = c.execute(r)
        self.assertTrue(rsp)
    
    def test_trade_bought_get(self):
        ''' TradesBoughtGetRequest can search we want?
        '''
        r = TradesBoughtGetRequest()
        r.set_fields('seller_nick,buyer_nick,title,type,created,sid,tid,seller_rate,buyer_rate,status,payment,\
                discount_fee,adjust_fee,post_fee,total_fee,pay_time,end_time,modified,consign_time,\
                buyer_obtain_point_fee,point_fee,real_point_fee,received_payment,commission_fee,pic_path,num_iid,\
                num_iid,num,price,cod_fee,cod_status,shipping_type,receiver_name,receiver_state,receiver_city,\
                receiver_district,receiver_address,receiver_zip,receiver_mobile,receiver_phone,orders.title,\
                orders.pic_path,orders.price,orders.num,orders.iid,orders.num_iid,orders.sku_id,orders.refund_status,\
                orders.status,orders.oid,orders.total_fee,orders.payment,orders.discount_fee,orders.adjust_fee,\
                orders.sku_properties_name,orders.item_meal_name,orders.buyer_rate,orders.seller_rate,\
                orders.outer_iid,orders.outer_sku_id,orders.refund_id,orders.seller_type')
        now = datetime.datetime(2011, 3, 1, 23, 11, 11)
        r.set_start_created(now.strftime('%Y-%m-%d %X'))
        #r.set_seller_nick(u'张三')
        #r.set_end_created(now.strftime('%Y-%m-%d %X'))
        #r.set_page_no('2')
        r.set_page_size('100')
        #r.set_status('WAIT_BUYER_PAY')
        rsp = c.execute(r)
        self.assertTrue(rsp)

class TestBadRequest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
