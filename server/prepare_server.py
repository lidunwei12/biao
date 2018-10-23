# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:09:35 2017

@author: boblee
"""
from http_api_exporter import ApiHttpServer
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
import src.data_prepare.word_frequency as prepare
from config import API


def prepare_server():
    app = ApiHttpServer()
    app.bind("/api/prepare", prepare.prepare_main)
    app.start(API.PORT_ONE)
    
    
if __name__ == "__main__":
    prepare_server()

