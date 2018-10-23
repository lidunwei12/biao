# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os
import subprocess

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def zip_main(zip_file, extract_home):
    output = subprocess.check_output('start winrar e ' + zip_file + ' ' + extract_home, stderr=subprocess.STDOUT,
                                     shell=True)
    return 'ok'
