'''@pytest_crypto

This file will test the cryptography functionalities with respect to
authentication.

'''
import imp
import yaml


def test_hashing():
    with open('/vagrant/hiera/settings.yaml', 'r') as stream:
        try:
            yamlres = yaml.load(stream)
            root = yamlres['general']['root']
            cryptopath = root + '/brain/converter/crypto.py'
        except yaml.YAMLError as error:
            print error
    crypto = imp.load_source('crypto', cryptopath)

    passwords = ['blue', 'red', 'green', 'yellow']

    for p in passwords:
        h1 = crypto.hashpass(p, app=False)
        h2 = crypto.hashpass(p, app=False)

        assert h1 != h2
        assert crypto.verifypass(p, h1, app=False)
        assert crypto.verifypass(p, h2, app=False)
