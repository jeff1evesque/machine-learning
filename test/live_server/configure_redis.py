'''

This module will FLUSHALL keys in the redis database.

'''

import subprocess


def configure_redis():
    '''

    Remove all keys from all existing redis database(s).

    '''

    # flush all redis keys
    subprocess.check_call(['redis-cli', 'FLUSHALL'])

    # assert FLUSHALL succeed
    count_keys = subprocess.check_call(['redis-cli', 'DBSIZE'])
    assert count_keys == 0
