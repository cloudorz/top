# coding: utf-8

import os, sys, urllib, urllib2, time, hashlib, json, logging, datetime
from logging.handlers import SMTPHandler, RotatingFileHandler


from .parsexml import xml2dict
from .user import UserGetRequest

DEBUG = True

#ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = '/tmp/toplogs'
if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)

class TopClient(object):
    ''' client for send request for TOP
    '''
    def __init__(self, key='test', secret='test', logger=None):
        # system args 
        self.app_key = key
        self.app_secret = secret
        self.base_url = 'http://gw.api.taobao.com/router/rest'
        #self.base_url = 'http://gw.api.tbsandbox.com/router/rest'
        self.format = 'json'
        self.sign_method = 'md5'
        self.api_version = '2.0'
        self.sdk_version = 'top-sdk-python-1.0'
        self.code_type = 'Python'
        
        # logger
        self.log_file = os.path.join(LOG_DIR, 'error.log')
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

        src = '%s%s%s' % (self.app_secret,
                ''.join('%s%s' % e for e in sorted(params.items())),
                self.app_secret)
        return hashlib.md5(src).hexdigest().upper()

    def config_logger(self):
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        debug_handler = RotatingFileHandler(self.log_file, maxBytes=10000, backupCount=5)
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(formatter)
        self.logger.addHandler(debug_handler)

    def log_communication_error(self, error_code, response_text):
        msg = 'the top communication error, error_no:%s, error message:%s' % (error_code, response_text)
        if DEBUG:
            print >> sys.stderr, msg
        self.logger.error(msg)

    def log_error(self, msg):
        if DEBUG:
            print >> sys.stderr, msg
        self.logger.debug(msg)

    def process_error(self, rsp):
        if 'error_response' in rsp:
            self.log_communication_error(rsp['error_response']['code'], rsp['error_response']['msg'])
            return True
        
    def process_data(self, rsp, path):
        # 获得有效数据数据
        for e in path.split('.'):
            rsp = rsp[e]
        return rsp

    def res2dict(self, res):
        if self.format == 'json':
            # json 格式的处理
            try:
                res = json.loads(res)
            except (ValueError, AttributeError),e:
                self.log_error('parse json data have errors')
                res = {}

        elif self.format == 'xml':
            # xml 格式的处理
            try:
                res = xml2dict(res)
            except Exception, e:
                self.log_error('parse xml data have errors')
                res = {}
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
        params.update(self.api_params)
        return params

    def execute(self, request, session=None):
        self.method = request.get_api_method_name()
        self.api_params = request.get_api_params()

        # 组装系统参数
        self.set_sys_params()

        if session:
            self.sys_params['session'] = session

        # 签名
        self.sys_params['sign'] = self.generate_sign(self.req_params())

        # 发送请求
        form_dict = urllib.urlencode(self.req_params())
        try:
            req = urllib2.urlopen(self.base_url, form_dict)
        except urllib2.HTTPError, e:
            self.log_error('have some error in req/resp')

        rsp = self.res2dict(req.read())
        if self.process_error(rsp):
            return

        return self.process_data(rsp, request.data_path)
