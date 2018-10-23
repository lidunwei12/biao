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
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def system_create(matrix_id, content_frequency_xls, level_three_xls, level_two_xls):
    status = 1
    save_home = DATA_HOME + '/' + str(matrix_id) + '/step_three/'
    index_home = DATA_HOME + '/' + str(matrix_id) + '/index/'
    try:
        content_check_main(content_frequency_xls, level_three_xls, save_home)
        level_two_handle(index_home, level_two_xls, save_home)
        level_two_excel = DATA_HOME + '/' + str(matrix_id) + '/step_three/二级指标.xls'
        level_three_excel = DATA_HOME + '/' + str(matrix_id) + '/step_three/三级指标.xls'
        final_xls(content_frequency_xls, level_two_excel, level_three_excel, save_home)
        create_index_matrix(DATA_HOME + '/' + str(matrix_id) + '/step_three/结果.xls', save_home)
        visual_cluster(DATA_HOME + '/' + str(matrix_id) + '/step_three/指标矩阵.csv', save_home)
        return {
            'matrix_id': matrix_id,
            'matrix_status': status,
            'index_matrix': DATA_HOME + '/' + str(matrix_id) + '/step_three/指标矩阵.csv',
            'heat_map': DATA_HOME + '/' + str(matrix_id) + '/step_three/heat_map.pdf',
            'level_two_cluster': DATA_HOME + '/' + str(matrix_id) + '/step_three/level_two_cluster.pdf',
            'level_three_cluster': DATA_HOME + '/' + str(matrix_id) + '/step_three/level_three_cluster',
            'data_ratio': DATA_HOME + '/' + str(matrix_id) + '/step_three/da_ratio.csv',
            'data_weights': DATA_HOME + '/' + str(matrix_id) + '/step_three/weight.xls'
        }
    except:
        return {
            'matrix_id': matrix_id,
            'matrix_status': 0,
            'index_matrix': '',
            'heat_map': '',
            'level_two_cluster': '',
            'level_three_cluster': '',
            'data_ratio': '',
            'data_weights': ''
        }
