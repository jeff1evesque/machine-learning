'''@crypto

This file contains various cryptography wrappers.


'''

from flask import current_app
import os
import hashlib
import base64

salt_length = current_app.config.get('SALT_LENGTH')


def hashpass(p):
    '''@hashpass

    This method returns a hash and salt from a password p

    @salt - a random string of saltlength bytes generated to hash the password

    '''
    global salt_length

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
