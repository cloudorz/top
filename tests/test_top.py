# coding: utf-8

import sys, unittest
sys.path.append('/Users/cloud/mywork/webdev/top')

from top import *

c = TopClient(key='12203314', secret='534ddb6e7b207c26e5b9752a34a1f920')

class TestTopRequest(unittest.TestCase):
    def test_user_get(self):
        ''' UserGetRequest can get right data?
        '''
        r = UserGetRequest()
        r.set_nick('mydewdew')
        r.set_fields('user_id,nick,location,udi,sex')

        rsp = c.execute(r)
        self.assertTrue(rsp and 'nick' in rsp and rsp['nick'] == 'mydewdew')

    def test_users_get(self):
        ''' UsersGetRequest can get right data?
        '''
        r = UsersGetRequest()
        r.set_nicks('mydewdew,84607362qq')
        r.set_fields('user_id,nick,location')
        rsp = c.execute(r)
        self.assertTrue(rsp and len(rsp)==2)

    def test_subscribe_get(self):
        ''' SubscribeGetRequest can get right data?
        '''
        r = SubscribeGetRequest()
        r.set_nick('mydewdew')

        rsp = c.execute(r)
        self.assertTrue(rsp)

class TestBadRequest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
