'''@pytest_crypto

This file will test the cryptography functionalities with respect to
authentication.

'''
import pytest
import imp
import os.path
import yaml


def test_hashing():
    with open("/vagrant/hiera/settings.yaml", 'r') as stream:
        try:
            cryptopath = yaml.load(stream)['crypto']['path']
        except yaml.YAMLError as exc:
            print exc

    crypto = imp.load_source('crypto', cryptopath)

    passwords = ['blue', 'red', 'green', 'yellow']

    for p in passwords: 
        h1 = crypto.hashpass(p)
        h2 = crypto.hashpass(p)
        assert h1 != h2
        assert crypto.verifypass(p, h1) and crypto.verifypass(p, h2)
