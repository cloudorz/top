# coding: utf-8

import sys
sys.path.append('/Users/cloud/mywork/webdev/top')

from top import TopClient, UserGetRequest, UsersGetRequest, SubscribeGetRequest

if __name__ == '__main__':
    t = TopClient()
    t.app_key = '12203314'
    t.app_secret = '534ddb6e7b207c26e5b9752a34a1f920'

    r = UserGetRequest()
    r.set_nick('mydewdew')
    r.set_fields('user_id,nick,location,uid,sex')

    r2 = UsersGetRequest()
    r2.set_nicks('mydewdew,84607362qq')
    r2.set_fields('user_id,nick,location,sex')

    r3 = SubscribeGetRequest()
    r3.set_nick('mydewdew')

    print t.execute(r)
    print t.execute(r2)
    print t.execute(r3)

