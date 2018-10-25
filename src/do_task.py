# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import time
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from src.data_prepare.word_frequency import prepare_main
from src.step_two.data_begin import begin_main
from src.step_three.system import system_create


def get_task(number):
    count = 0
    for i, line in enumerate(open(rootPath + "/task.txt", "r",encoding='utf8')):
        if i >= number:
            line = line.strip('\n')
            temp_ = str(line).split(' ')
            if len(temp_)==4:
                if temp_[1] == 'step_one':
                    prepare_main(temp_[0], temp_[2], temp_[3])
            if len(temp_) == 6:
                if temp_[1] == 'step_two':
                    begin_main(temp_[0], temp_[2], temp_[3], temp_[4], temp_[5])
            if len(temp_) == 4:
                if temp_[1] == 'step_three':
                    system_create(temp_[0], temp_[2], temp_[3])
        count = count + 1
    return count


def execute_main():
    """
             主函数
             功能: 每隔5秒，获取数据库的状态
         """
    number = 0
    while 1:
        number = get_task(number)
        time.sleep(2)


execute_main()