#!/usr/bin/python

'''

This file can set, or get the required redis host, or port.

'''

from flask import current_app


class Settings:
    '''

    This class provides an interface to get, or set the redis host, or redis
    port.

    '''

    def __init__(self):
        '''

        This constructor defines the default redis host, and redis port.

        '''

        self.host = current_app.config.get('CACHE_HOST')
        self.port = current_app.config.get('CACHE_PORT')

    def get_host(self):
        '''

        This method returns the redis host, associated with this class
        instance.

        '''

        return self.host

    def get_port(self):
        '''

        This method returns the redis port, associated with this redis
        instance.

        '''

        return self.port

    def set_host(self, host):
        '''

        This method sets the redis host attribute, associated with this class
        instance.

        '''

        self.host = host

    def set_port(self, port):
        '''

        This method sets the redis port attribute, associated with this class
        instance.

        '''

        self.port = port
