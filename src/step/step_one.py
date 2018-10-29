# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os
import subprocess
import random
import time

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
run_home = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def zip_main(zip_file, extract_home):
    output = subprocess.check_output('start winrar e -o+ ' + zip_file + ' ' + extract_home, stderr=subprocess.STDOUT,
                                     shell=True)
    return 'ok'


def generate_random_str(random_length):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'abcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(random_length):
        random_str += base_str[random.randint(0, length)]
    return random_str


def prepare_one(content_name, catalog_name):
    content_name = 'D:/data-mining/data' + content_name
    catalog_name = 'D:/data-mining/data' + catalog_name
    prepare_id = generate_random_str(4)
    temp_home = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/' + str(prepare_id)))
    if not os.path.isdir(temp_home):
        os.mkdir(temp_home)
    home = ['content/', 'index/', 'step_one/', 'step_two/', 'step_three/']
    for s in home:
        make_home = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/' + str(prepare_id) + '/' + s))
        if not os.path.isdir(make_home):
            os.mkdir(make_home)
    zip_main(content_name, DATA_HOME + '/' + str(prepare_id) + '/content/')
    zip_main(catalog_name, DATA_HOME + '/' + str(prepare_id) + '/index/')
    count_content = sum([len(x) for _, _, x in os.walk(DATA_HOME + '/' + str(prepare_id) + '/content/')])
    count_index = sum([len(x) for _, _, x in os.walk(DATA_HOME + '/' + str(prepare_id) + '/index/')])
    if count_content != 0 and count_index != 0:
        content_home = DATA_HOME + '/' + str(prepare_id) + '/content/'
        index_home = DATA_HOME + '/' + str(prepare_id) + '/index/'
        f = open(run_home + '/task.txt', "a", encoding='utf8')
        f.write(prepare_id + ' step_one' + ' ' + content_home + ' ' + index_home + '\n')
        f.close()
        with open(run_home + "/status.txt", "a", encoding='utf8') as f:
            f.write(prepare_id + ' 准备挖掘中 ' + '\n')
            f.close()
        return {
            'prepare_id': prepare_id,
        }
    else:
        with open(run_home + "/status.txt", "a", encoding='utf8') as f:
            f.write(prepare_id + ' 准备挖掘失败 ' + '\n')
            f.close()
        return {
            'prepare_id': '',
        }
