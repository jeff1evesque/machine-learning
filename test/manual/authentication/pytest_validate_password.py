'''

This file will test the password validation functionality.

'''

import imp
import yaml


def test_validate_password():
    with open('/vagrant/hiera/common.yaml', 'r') as stream:
        try:
            yamlres = yaml.load(stream)
            root = yamlres['general']['root']
            validate_password = root + '/brain/validator/validate_password.py'
            vp = imp.load_source('validate_password', validate_password)
        except yaml.YAMLError as error:
            print error

    passwords = [
        'abcdefghij123',  # just right
        'ABCDEFGHIJ123',  # just right
        'abcDEFGHIJ123',  # just right
        'abcdefgh1',      # too short
        'abcdefghijk',    # no numbers
        '12345678911',    # no letters
        'abcdefghIJK',    # no numbers
        'a1' * 65         # too long
    ]

    answers = [
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False
    ]

    assert map(
        lambda p: vp.validate_password(p, app=False),
        passwords
    ) == answers
