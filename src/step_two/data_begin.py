# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
from src.step_two.content_create import content_main
from src.step_two.index_create import index_main
import os

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def begin_main(id, measure_xls, content_frequency, index_library, index_frequency):
    status = 1
    try:
        content_home = DATA_HOME + str(id) + '/content/'
        save_home = DATA_HOME + str(id) + '/step_one'
        content_main(content_home, measure_xls, content_frequency, save_home)
        index_home = DATA_HOME + str(id) + '/index/'
        index_main(save_home, index_library, index_home)
    except:
        status = 0
    return {
        'status': status
    }
