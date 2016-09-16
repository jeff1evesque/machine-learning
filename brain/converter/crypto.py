'''@crypto

This file contains various cryptography wrappers.


'''

import os
import hashlib
import base64
import yaml

with open("/vagrant/hiera/settings.yaml", 'r') as stream:
    try:
        salt_length = yaml.load(stream)['crypto']['salt_length']
    except yaml.YAMLError as error:
        print(error)
		

def hashpass(p):
    '''@hashpass

    This method returns a hash and salt from a password p

    @salt - a random string of saltlength bytes generated to hash the password

    '''

    salt = base64.b64encode(os.urandom(salt_length))
    return hashlib.sha512(salt + p).hexdigest()+"$"+salt


def verifypass(p, h):
    '''@verifypass

    This function verifies that a password p hashes to a hash h as
    returned by hashpass.

    @h - hash extracted from the hash+salt
    @s - salt extracted from the hash+salt

    '''

    h, s = h.split('$')
    return hashlib.sha512(s + p).hexdigest() == h
