#!/usr/bin/python

import cgi

print('Content-type: text/html \n\n')
form = cgi.FieldStorage()
temp  = form['svm_session'].value

print('here: ' + temp)
