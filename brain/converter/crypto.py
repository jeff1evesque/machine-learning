'''@crypto

This file contains various cryptography wrappers.


'''

from flask import current_app
import os
import base64
import yaml
import scrypt


def getsalt(app=True, root='/vagrant'):
    '''@getsalt

    This method returns the salt.

    @app, indicates if function is to be used by application, or manually

    '''
    if app:
        salt_length = current_app.config.get('SALT_LENGTH')
        return base64.b64encode(os.urandom(salt_length))
    else:
        with open(root + "/hiera/settings.yaml", 'r') as stream:
            try:
                salt_length = yaml.load(stream)['crypto']['salt_length']
                return base64.b64encode(os.urandom(salt_length))
            except yaml.YAMLError as error:
                return base64.b64encode(os.urandom(32))


def getscryptparams(app=True, root='/vagrant'):
    '''@getscryptparams

    This method returns the parameters N,r,p for the scrypt function.
    
    Note: No minimum is enforced for these parameters because a minimum can
    potentially break the hashing function in a system incapable of meeting
    those requirements

    @app, indicates if function is to be used by application, or manually

    '''
    if app:
        N = current_app.config.get('SCRYPT_N')
        r = current_app.config.get('SCRYPT_R')
        p = current_app.config.get('SCRYPT_P')
	return pow(2,N), r, p
    else:
        with open(root + "/hiera/settings.yaml", 'r') as stream:
            try:
           	yamlstream = yaml.load(stream)
                N = yamlstream['crypto']['scrypt_n']
                r = yamlstream['crypto']['scrypt_r']
                p = yamlstream['crypto']['scrypt_p']
                return pow(2,N), r, p
            except yaml.YAMLError as error:
                return pow(2,18), 8, 1


def hashpass(p):
    '''@hashpass

    This method returns a hash and salt from a password p

    @salt - a random string of saltlength bytes generated to hash the password

    '''
    salt = getsalt(app=False)
    N,r,p = getscryptparams(app=False)
    try:
        hashed = scrypt.hash(p, salt, N=N, r=r, p=p, buflen=512)
        hashed = hashed.encode("hex")
        return hashed + "$" + salt
    except scrypt.error:
        return False


def verifypass(p, h):
    '''@verifypass

    This function verifies that a password p hashes to a hash h as
    returned by hashpass.

    @h - hash extracted from the hash+salt
    @s - salt extracted from the hash+salt

    '''
    h, s = h.split('$')
    hashed = scrypt.hash(p, s, N=pow(2,18), r=8, p=1, buflen=512).encode("hex")
    return hashed == h
