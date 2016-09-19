'''@crypto

This file contains various cryptography wrappers.


'''

from flask import current_app
import os
import hashlib
import base64
import yaml


def load_salt(app=True, root='/vagrant'):
    '''@load_salt

    This method returns the salt length.

    @app, indicates if function is to be used by application, or manually

    '''
    if app:
        salt_length = current_app.config.get('SALT_LENGTH')
        return {'salt_length': salt_length, 'error': None}
    else:
        with open(root + "/hiera/settings.yaml", 'r') as stream:
            try:
                salt_length = yaml.load(stream)['crypto']['salt_length']
                return {'salt_length': salt_length, 'error': None}
            except yaml.YAMLError as error:
                return {'salt_length': None, 'error': error}

				
def hashpass(p):
    '''@hashpass

    This method returns a hash and salt from a password p

    @salt - a random string of saltlength bytes generated to hash the password

    '''
    salt_length = load_salt(app=False)['salt_length']
    salt_length = salt_length if salt_length is not None else 32
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
