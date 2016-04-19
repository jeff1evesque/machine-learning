#!/usr/bin/python

'''## @data_new

This file allows methods defined from the Base, or Base_Data superclass to be
overridden, if needed.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.session.base import Base
from brain.session.base_data import Base_Data


class Data_New(Base, Base_Data):
    '''@Data_New

    This class provides a generic constructor interface.

    Note: this class is invoked within 'load_data.py'

    Note: inherit base methods from superclass 'Base', 'Base_Data

    '''

    def __init__(self, svm_data):
        '''@__init__

        This constructor defines class properties using the superclass 'Base',
        and 'Base_Data' constructor, along with the constructor in this
        subclass.

        @super(), implement 'Base', and 'Base_Data' superclass constructor
            within this child class constructor.

        @self.uid, the logged-in user (i.e. userid).

        Note: the superclass constructor expects the same 'svm_data' argument.

        '''

        super(Data_New, self).__init__(svm_data)
        self.observation_labels = []
        self.list_error = []
        self.uid = 1
