# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:00:46 2017

@author: boblee
"""
import urllib.request
import json
from config import API


def data_system(matrix_id, level_three_xls, level_two_xls):
    values = {'matrix_id': matrix_id,
              'level_three_xls': level_three_xls, 'level_two_xls': level_two_xls}
    url = "http://" + str(API.IP) + ":" + str(API.PORT_THREE) + "/api/system"
    data = json.dumps(values).encode("utf8")
    res = urllib.request.Request(url, data, {'Content-Type': 'application/json'})
    try:
        resp = urllib.request.urlopen(res)
        contents = resp.read()
    except urllib.error.URLError as e:
        contents = e.read()
    return json.loads(contents)


print(data_system('sbbr', '/test/三级指标人工修正表re.xls',
                 '/test/二级指标人工处理中re.xls',))
