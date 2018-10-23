# -*- coding: utf-8 -*-
"""
Created on Thu May 25 09:09:35 2017

@author: boblee
"""
import os
import sys
import src.step_two.data_begin as begin
import src.data_prepare.word_frequency as prepare
# import src.step_three.system as system
from http_api_exporter import ApiHttpServer

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def prepare_server():
    app = ApiHttpServer()
    app.bind("/api/prepare", prepare.prepare_main)
    app.start(8888)


def begin_server():
    app = ApiHttpServer()
    app.bind("/api/begin", begin.begin_main)
    app.start(8887)


# def system_server():
#     app = ApiHttpServer()
#     app.bind("/api/system", system.system_create)
#     app.start(8886)
    
    
if __name__ == "__main__":
    prepare_server()
    # begin_server()
