# coding: utf-8
'''
the base class of all request for top api 
'''

from abc import ABCMeta, abstractmethod

class Request(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_api_method_name(self):
        pass
    
    @abstractmethod
    def get_api_params(self):
        pass

    #@abstractmethod
    #def get_data(self, rsp):
    #    pass
