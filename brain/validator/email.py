'''

This file validates email addresses.

'''

import re


def isValidEmail(email):
    '''

    This method checks if the supplied email matches the accepted regex email
    pattern. If not matches are found, the function will return 'false'.

    '''

    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    match = re.match(regex, email)

    if match == None:
        return False
    return True
