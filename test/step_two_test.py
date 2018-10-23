# -*- coding: utf-8 -*-
"""
Created on Thu May 25 11:00:46 2017

@author: boblee
"""
import urllib.request
import json
from config import API


def data_begin(begin_id, classifier_form, content_frequency, catalog_index_form, catalog_frequency):
    values = {'begin_id': begin_id, 'classifier_form': classifier_form, 'content_frequency': content_frequency,
              'catalog_index_form': catalog_index_form, 'catalog_frequency': catalog_frequency}
    url = "http://" + str(API.IP) + ":" + str(API.PORT_TWO) + "/api/begin"
    data = json.dumps(values).encode("utf8")
    res = urllib.request.Request(url, data, {'Content-Type': 'application/json'})
    try:
        resp = urllib.request.urlopen(res)
        contents = resp.read()
    except urllib.error.URLError as e:
        contents = e.read()
    return json.loads(contents)
