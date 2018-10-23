# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:00:46 2017

@author: boblee
"""
import re
import os
DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)

def api_text():
    ip_address = '192.168.20.240'
    step_one_port = 8888
    step_two_port = 8887
    step_three_port = 8886
    for line in open(DATA_HOME+'/config.ini'):
        line = line.replace('\n', '')
        if line.find('ip =') != -1:
            ip_address = line[line.find('ip =') + 4:].replace(' ', '')
        if line.find('step_one') != -1:
            step_one_port = int(re.findall(re.compile('\d+'), line)[0])
        if line.find('step_two') != -1:
            step_two_port = int(re.findall(re.compile('\d+'), line)[0])
        if line.find('step_three') != -1:
            step_three_port = int(re.findall(re.compile('\d+'), line)[0])
    return ip_address, step_one_port, step_two_port, step_three_port


class API:
    ip_address, step_one_port, step_two_port, step_three_port = api_text()
    IP = ip_address
    PORT_ONE = step_one_port
    PORT_TWO = step_two_port
    PORT_THREE = step_three_port
