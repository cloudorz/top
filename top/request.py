# coding: utf-8

from abc import ABCMeta, abstractmethod

class Request(object):
    __metaclass__ = ABCMeta

    def get_api_method_name(self):
        return self.method
    
    def get_api_params(self):
        return self.p

    def get_data_path(self):
        return '_'.join(self.method.split('.')[1:]+['response'])

    #@abstractmethod
    #def get_data(self, rsp):
    #    pass
