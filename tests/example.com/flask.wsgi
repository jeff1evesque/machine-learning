#!/bin/env python2.7
import sys
sys.path.insert(0, "/var/www/html/public_html/example.com")

activate_this = '/var/www/html/public_html/example.com/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from app import app as application
