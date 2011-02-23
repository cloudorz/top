# coding: utf-8

import os, sys, urllib, urllib2, time, hashlib, json, logging
from logging.handler import SMTPHandler, RotatingFileHandler

from .parsexml import xml2dict

ROOT_DIR = os.path.dirname(os.path.abspath(__name__))

class TopClient(object):
    ''' client for send request for TOP
    '''
    def __init__(self, logger=None):
        # system args 
        self.app_key = 'test'
        self.app_secret = 'test'
        self.base_url = 'http://gw.api.tabobao.com/router/rest'
        self.test_url = 'http://gw.sandbox.tabobao.com/router/rest'
        self.format = 'json'
        self.sign_method = 'md5'
        self.api_version = '2.0'
        self.sdk_version = 'top-sdk-python-1.0'
        self.code_type = 'Python'
        
        # logger
        self.log_file = os.path.join(ROOT_DIR, 'logs/error.log')
        self.logger = logger or logging.getLogger()
        self.config_logger()

    def generate_sign(self, params):
        ''' generate sign
        '''
        for k,v in params.items():
            if not v.startswith('@'): # 不是文件上传
                try:
                    params[k] = v.encode('utf-8')
                except AttributeError:
                    pass

        src = self.app_secret + ''.join('%s%s' % (k,v) for k,v in sorted(params.items()))
        return hashlib.md5(src).hexdigest().upper()

    def config_logger(self):
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s ',
            '[in %(pathname)s:%(lineno)d]')
        debug_handler = RotatingFileHandler(self.log_file, maxBytes=10000, backupCount=5)
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(debug_handler)
        self.logger.addHandler(debug_handler)

    def log_error(self, api_name, url, error_code, response_text):
        # TODO 系统错误日志
        self.logger.log('')

    def process_error(self, rsp)
        if 'error_response' in rsp:
            self.log_error(rsp['error_response']['code'], rsp['error_response']['msg'])
        else:
            return True
        
    def process_data(self, rsp):
        # 获得有效数据数据
        return rsp.values()[0].values()[0]

    def res2dict(self, res):
        if self.format == 'json':
            # json 格式的处理
            try:
                res = json.loads(res)
            except AttributeError,e:
                self.log_error(e)
                return

        elif self.format == 'xml':
            # xml 格式的处理
            try:
                res = xml2dict(res)
            except Exception, e:
                self.log_error(e)
        else:
            res = {}
            self.log_error(u'返回了不支持的数据格式')
        return res

    def set_sys_params(self):
        self.sys_params = {
                'app_key':self.app_key,
                'v':self.api_version,
                'method':self.method,
                'format':self.format,
                'sign_method':self.sign_method,
                'timestamp':datetime.datetime.now().strftime('%Y-%m-%d %X'),
                'partner_id':self.sdk_version,
                'codeType':self.code_type,
                }

    def req_params(self):
        params = {}
        params.update(self.sys_params)
        params.udpate(self.api_params)
        return params

    def execute(self, request, session=None):
        self.method = request.get_api_method_name()
        self.api_params = request.get_api_params()

        # 组装系统参数
        sef.set_sys_params()

        if session:
            self.sys_params['session'] = session

        # 签名
        self.sys_params['sign'] = self.generate_sign(self.req_params())

        # 发送请求
        form_dict = urllib.urlencode(self.req_params())
        try:
            req = urllib2.urlopen(self.base_url, form_dict)
        except Exception, e:
            self.log_error(e)
            return

        rsp = self.res2dict(req.read())
        if self.process_error(rsp):
            return 

        return self.process_data(rsp, request.get_data)

