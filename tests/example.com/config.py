# Enable Development Env

DEBUG = True

# Application Directory

import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the db

SQLALCHEMY_DATABASE_URI = 'mysql://phat:ph4t@localhost/phatdb'
DATABASE_CONNECT_OPTIONS = {}

# Application threads. Common assumption is
# to use 2 threads per available core.
# Handles incoming requests using one and 
# performs background operations on other.

THREADS_PER_PAGE = 2

# CSRF

CSRF_ENABLED = True
CSRF_SESSION_KEY = '7NM7jjpxCxVmT4JHnU1TsRIhKbbsubUdPT4lBoLlbxA8XA71cBQk3jXT6hp'

# Key for cookies

SECRET_KEY = '5hgbKwlm3vz1gRrtO0QTsACTqMbKVWbIFz1t2E6Utw8Ppft5qpWpARvFWIPJi00'
