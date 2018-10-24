# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
from src.step_two.content_create import content_main
from src.step_two.index_create import index_main
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def begin_main(begin_id, classifier_form, content_frequency, catalog_index_form, catalog_frequency):
    status = 1
    try:
        content_home = DATA_HOME + '/' + str(begin_id) + '/content/'
        save_home = DATA_HOME + '/' + str(begin_id) + '/step_two'
        content_main(content_home, classifier_form, content_frequency, save_home)
        index_home = DATA_HOME + '/' + str(begin_id) + '/index/'
        index_main(save_home, catalog_index_form, index_home)
        return {
            'begin_id': begin_id,
            'status': status,
            'level_two_untreated': DATA_HOME + '/' + str(begin_id) + '/step_two/二级指标人工修正表.xls',
            'level_three_untreated': DATA_HOME + '/' + str(begin_id) + '/step_two/三级指标人工修正表.xls'
        }
    except:
        status = 0
        return {
            'begin_id': begin_id,
            'status': status,
            'level_two_untreated': '',
            'level_three_untreated': ''
        }
