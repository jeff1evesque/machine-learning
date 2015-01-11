#!/usr/bin/python

## @session_model_generate.py
#  This file receives data (i.e. settings) required to query from the database a
#      previously stored session, involving one or more stored dataset uploads,
#      and generates a corresponding SVM model. The new SVM model, is stored into
#      a database table, which later can be retrieved via 'session_model_use.py'.

