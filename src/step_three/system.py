# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
from src.step_three.content_check import content_check_main
from src.step_three.index import level_two_handle
from src.step_three.to_new import final_xls
from src.step_three.to_new import create_index_matrix
from src.step_three.final_create import visual_cluster
import os

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def system_create(id, content_frequency_xls, level_three_xls, level_two_xls):
    status = 1
    save_home = DATA_HOME + str(id) + '/step_three/'
    index_home = DATA_HOME + str(id) + '/index/'
    content_check_main(content_frequency_xls, level_three_xls, save_home)
    level_two_handle(index_home, level_two_xls, save_home)
    level_two_excel = DATA_HOME + str(id) + '/step_three/二级指标.xls'
    level_three_excel = DATA_HOME + str(id) + '/step_three/三级指标.xls'
    final_xls(content_frequency_xls, level_two_excel, level_three_excel, save_home)
    create_index_matrix(DATA_HOME + str(id) + '/step_three/结果.xls', save_home)
    visual_cluster(DATA_HOME + str(id) + '/step_three/指标矩阵.csv', save_home)
    return {
        'status': status
    }
