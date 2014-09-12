#!/usr/bin/python

## @svm_training.py
#  This file properly escapes POST data received from 'php/logic_loader.php',
#      parses the data, and sends respective portions of the POST data to
#      'python/data_creator.py'. data_creator.py is responsible for saving
#      the SVM dataset into the mySQL database.
#
#  @import sys, provides various functions, and variables that can be used to
#      manipulate different parts of the Python runtime environment (i.e. argv).

import sys

# temporarily check if arguments are passed in
print 'test string'#sys.argv[1:]
