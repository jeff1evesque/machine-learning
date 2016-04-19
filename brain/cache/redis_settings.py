#!/usr/bin/python

'''@redis_settings

This file can set, or get the required redis host, or port.

'''

from settings import HOST, PORT_REDIS


class Redis_Settings(object):
    '''@Redis_Settings

    This class provides an interface to get, or set the redis host, or redis
    port.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self):
        '''@__init__

        This constructor defines the default redis host, and redis port.

        '''

        self.host = HOST
        self.port = PORT_REDIS

    def get_host(self):
        '''@get_host

        This method returns the redis host, associated with this class
        instance.

        '''

        return self.host

    def get_port(self):
        '''@get_port

        This method returns the redis port, associated with this redis
        instance.

        '''

        return self.port

    def set_host(self, host):
        '''@set_host

        This method sets the redis host attribute, associated with this class
        instance.

        '''

        self.host = host

    def set_port(self, port):
        '''@set_host

        This method sets the redis port attribute, associated with this class
        instance.

        '''

        self.port = port
