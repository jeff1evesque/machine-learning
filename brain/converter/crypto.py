'''

This file contains various cryptography wrappers.

'''

from flask import current_app
import os
import base64
import yaml
import scrypt


def getsalt(app=True, root='/vagrant'):
    '''

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
            except:
                return base64.b64encode(os.urandom(32))


def getscryptparams(app=True, root='/vagrant'):
    '''

    This method returns the parameters N,r,p for the scrypt function.

    @N - work factor (iteration count). N must be power of 2, so the settings
         value indicates the exponent.
    @r - blocksize for underlying hash. Should be increased based on memory
         improvement.
    @p - parallelization factor. Should be increased based on CPU improvement.

    Note: No minimum is enforced for these parameters because a minimum can
    break the hashing function in a system incapable of meeting those
    requirements.

    @app, indicates if function is to be used by application, or manually

    '''

    if app:
        N = current_app.config.get('SCRYPT_N')
        r = current_app.config.get('SCRYPT_R')
        p = current_app.config.get('SCRYPT_P')
        return pow(2, N), r, p
    else:
        with open(root + "/hiera/settings.yaml", 'r') as stream:
            try:
                yamlstream = yaml.load(stream)
                N = yamlstream['crypto']['scrypt_n']
                r = yamlstream['crypto']['scrypt_r']
                p = yamlstream['crypto']['scrypt_p']
                return pow(2, N), r, p
            except:
                return pow(2, 18), 8, 1


def hashpass(password, app=True):
    '''

    This method returns a hash and salt from a password p

    @salt - a random string of saltlength bytes generated to hash the password

    '''

    salt = getsalt(app=app)
    N, r, p = getscryptparams(app=app)
    try:
        hashed = scrypt.hash(password, salt, N=N, r=r, p=p, buflen=512)
        hashed = hashed.encode("hex")
        return hashed + "$" + salt
    except scrypt.error:
        return False


def verifypass(password, h, app=True):
    '''

    This function verifies that a password p hashes to a hash h as
    returned by hashpass.

    @h - hash extracted from the hash+salt
    @s - salt extracted from the hash+salt

    '''

    N, r, p = getscryptparams(app=app)
    h, s = h.split('$')
    hashed = scrypt.hash(password, s, N=N, r=r, p=p, buflen=512)
    hashed = hashed.encode("hex")
    return hashed == h
