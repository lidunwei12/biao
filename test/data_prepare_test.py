# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:00:46 2017

@author: boblee
"""
import urllib.request
import json
import socket

ip_address = socket.gethostbyname(socket.getfqdn(socket.gethostname()))


def data_prepare(id, measure_xls, content_frequency, index_library, index_frequency):
    values = {'id': id, 'measure_xls': measure_xls, 'content_frequency': content_frequency,
              'index_library': index_library, 'index_frequency': index_frequency}
    url = "http://" + str(ip_address) + ":8888/api/prepare"
    data = json.dumps(values).encode("utf8")
    res = urllib.request.Request(url, data, {'Content-Type': 'application/json'})
    try:
        resp = urllib.request.urlopen(res)
        contents = resp.read()
    except urllib.error.URLError as e:
        contents = e.read()
    return json.loads(contents)


print(data_prepare('E:/work/content_main/content_biao/temp/政策性文件.zip', 'E:/work/content_main/content_biao/temp/目录.zip'))
