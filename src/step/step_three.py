# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os
from src.step.step_two import check_main

home = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))


def matrix_task(matrix_id, level_three_xls, level_two_xls):
    count = 0
    temp_ = [level_three_xls, level_two_xls]
    for j in temp_:
        count = count + check_main(j)
    if count == 0:
        with open(home + "/task.txt", "a", encoding='utf8') as f:
            f.write(
                matrix_id + 'step_three' + ' ' + level_three_xls + ' ' + level_two_xls + '\n')
            f.close()
        with open(home + "/status.txt", "a", encoding='utf8') as f:
            f.write(matrix_id + ' 待生成指标矩阵' + '\n')
            f.close()
        return {
            'status': 1
        }
    else:
        return {
            'status': 0
        }
