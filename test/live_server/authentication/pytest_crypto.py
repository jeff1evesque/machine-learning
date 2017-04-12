'''

This file will test the cryptography functionalities with respect to
authentication.

'''
import imp


def test_hashing():
    root = '/var/machine-learning'

    try:
        cryptopath = root + '/brain/converter/crypto.py'
        crypto = imp.load_source('crypto', cryptopath)
    except Exception as error:
        print error

    passwords = ['blue', 'red', 'green', 'yellow']

    for p in passwords:
        h1 = crypto.hash_pass(p, app=False)
        h2 = crypto.hash_pass(p, app=False)

        assert h1 != h2
        assert crypto.verify_pass(p, h1, app=False)
        assert crypto.verify_pass(p, h2, app=False)
