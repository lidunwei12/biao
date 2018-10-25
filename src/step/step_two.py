# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os
import xlrd

home = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))


def check_main(xls_name):
    status = 0
    try:
        workbook = xlrd.open_workbook(xls_name)
        sheet_number = workbook.sheet_names()
        if len(sheet_number) != 1:
            status = 1
        else:
            sheet = sheet_number[0]
            sheet_ = workbook.sheet_by_name(sheet)
            if sheet_.nrows == 0 or sheet_.ncols == 0:
                status = 1
    except:
        status = 1
    return status


def begin_task(begin_id, classifier_form, content_frequency, catalog_index_form, catalog_frequency):
    count = 0
    temp_ = [classifier_form, content_frequency, catalog_index_form, catalog_frequency]
    for j in temp_:
        count = count + check_main(j)
    if count == 0:
        with open(home + "/task.txt", "a", encoding='utf8') as f:
            f.write(
                begin_id + ' ' + 'step_two' + ' ' + classifier_form + ' ' + content_frequency + ' ' + catalog_index_form + ' ' + catalog_frequency + '\n')
            f.close()
        with open(home + "/status.txt", "a", encoding='utf8') as f:
            f.write(begin_id + ' 待开始挖掘挖掘中 ' + '\n')
            f.close()
        return {
            'status': 1
        }
    else:
        return {
            'status': 0
        }
