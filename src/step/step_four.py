# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os

home = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))

status_name = {'准备挖掘中': 0, '待开始挖掘挖掘中 ': 1, '准备挖掘成功': 2, '准备挖掘失败': 3, '开始挖掘中': 4, '开始挖掘成功': 5, '开始挖掘失败': 6, '待生成指标矩阵': 7,
               '生成指标矩阵中': 8,'生成指标矩阵成功':9,'生成指标矩阵失败':10}


def status_task(task_id):
    status = '准备挖掘中'
    file = []
    content = []
    for line in open(home + "/status.txt", "r", encoding='utf8'):
        if line.find(task_id) != -1:
            line = line.strip('\n')
            content.append(line)
    content_status = []
    status_content = []
    for m in content:
        if m.find('成功') != -1 or m.find('失败') != -1:
            content_status.append(m)
        else:
            status_content.append(m)
    if len(content_status) != 0:
        for i in range(len(content_status)):
            temp_content = content_status[i]
            temp_ = temp_content.split(' ')
            for j in range(2, len(temp_)):
                if temp_[j]:
                    for key, value in status_name.items():
                        if key == temp_[1]:
                            file.append([value, temp_[j]])
        temp_content = content_status[len(content_status) - 1]
        temp_ = temp_content.split(' ')
        status = temp_[1]
        # if len(temp_) > 2:
        #     file = temp_content[temp_content.index(temp_[2]):]
    elif len(status_content) != 0:
        temp_content = status_content[0]
        temp_ = temp_content.split(' ')
        status = temp_[1]
    return {
        'status': status,
        'file': file
    }


# print(status_task('xpct'))
