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
import src.step.step_four as status
from config import API


def status_server():
    app = ApiHttpServer()
    app.bind("/api/status", status.status_task)
    app.start(API.PORT_FOUR)


if __name__ == "__main__":
    status_server()

