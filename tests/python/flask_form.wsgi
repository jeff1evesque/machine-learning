## flask_form.wsgi
#  This file will import the main 'flask' application object, and
#  execute it within the WSGI Apache module.

import sys
sys.path.insert(0, '/var/www/html/machine-learning/tests/python/')
from flask_form import app as application
