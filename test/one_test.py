# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:00:46 2017

@author: boblee
"""
import urllib.request
import json
from config import API


def data_prepare(content_file, catalog_file):
    values = {'content_name': content_file, 'catalog_name': catalog_file}
    url = "http://" + str(API.IP) + ":"+str(API.PORT_ONE)+"/api/prepare"
    data = json.dumps(values).encode("utf8")
    res = urllib.request.Request(url, data, {'Content-Type': 'application/json'})
    try:
        resp = urllib.request.urlopen(res)
        contents = resp.read()
    except urllib.error.URLError as e:
        contents = e.read()
    return json.loads(contents)


print(data_prepare('E:/biao/temp/pdf2docx.zip', 'E:/biao/temp/区域质量.rar'))
