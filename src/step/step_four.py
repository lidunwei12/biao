# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os

home = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))


def status_task(task_id):
    status = '准备挖掘中'
    file = ''
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
        temp_content = content_status[len(content_status) - 1]
        temp_ = temp_content.split(' ')
        status = temp_[1]
        if len(temp_) > 2:
            file = temp_content[temp_content.index(temp_[2]):]
    elif len(status_content) != 0:
        temp_content = status_content[len(status_content) - 1]
        temp_ = temp_content.split(' ')
        status = temp_[1]
    return {
        'status': status,
        'file': file
    }
# print(status_task('s15n'))
