# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import xlrd
import numpy as np
from xlwt import Workbook
import pandas as pd
import os

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def final_xls(frequency_xls, level_two_xls, level_three_xls, save_home):
    """
         子函数:合并前面生成的二级指标、三级指标
         :param: frequency_xls:内容分词表路径
         :param: frequency_sheet:内容分词表表名
         :param: level_two_xls:二级指标表路径
         :param: level_two_sheet:二级指标表表名
         :param: level_three_xls:三级指标表路径
         :param: level_three_sheet:三级指标表表名
         :param: save_home:结果表保存路径
         """
    workbook = xlrd.open_workbook(frequency_xls)
    sheet_one = workbook.sheet_by_name('list')
    content_word = []
    for i in range(sheet_one.nrows):
        data = []
        for j in range(sheet_one.ncols):
            result = sheet_one.cell(i, j).value
            if type(result) == 'float':
                result = int(result)
            data.append(result)
        content_word.append(data)
    content_word = np.reshape(np.array(content_word), (sheet_one.nrows, sheet_one.ncols))
    name = []
    for i in range(sheet_one.nrows):
        if i == 0:
            name.append('频率汇总')
        else:
            name.append('')
    name = np.reshape(np.array(name), (sheet_one.nrows, 1))
    content_word = np.append(content_word, name, axis=1)
    workbook_level_three = xlrd.open_workbook(level_three_xls)
    sheet_level_three = workbook_level_three.sheet_by_name('list')
    content_level_three = []
    for i in range(sheet_level_three.nrows):
        data = []
        for j in range(sheet_level_three.ncols):
            result = sheet_level_three.cell(i, j).value
            data.append(result)
        content_level_three.append(data)
    content_level_three = np.reshape(np.array(content_level_three), (sheet_level_three.nrows, sheet_level_three.ncols))
    print(content_word.shape)
    print(content_level_three.shape)
    final_sheet = np.append(content_word, content_level_three, axis=1)
    workbook_level_two = xlrd.open_workbook(level_two_xls)
    sheet_level_two = workbook_level_two.sheet_by_name('list')
    content_level_two = []
    for i in range(sheet_level_two.nrows):
        data = []
        for j in range(sheet_level_two.ncols):
            result = sheet_level_two.cell(i, j).value
            data.append(result)
        content_level_two.append(data)
    content_level_two = np.reshape(np.array(content_level_two), (sheet_level_two.nrows, sheet_level_two.ncols))
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('Sheet4')
    for i, line in enumerate(final_sheet.tolist()):
        if len(line) > 256:
            line = line[0:255]
        for j, m in enumerate(line):
            sheet1.write(i, j, m)
    sheet2 = book.add_sheet('Sheet2')
    for i, line in enumerate(content_level_two.tolist()):
        for j, m in enumerate(line):
            sheet2.write(i, j, m)
    book.save(save_home + '/结果.xls')


def create_index_matrix(index_xls, save_home):
    """
    子函数:根据二级、三级指标词频矩阵，生成二级、三级关系矩阵，对应Step 4
    :param: index_xls:词频excel文件
    :param: level_two_sheet:二级词频表
    :param: level_three_sheet:三级词频表
    :param: save_home:关系矩阵表
    """
    workbook = xlrd.open_workbook(index_xls)
    sheet_one = workbook.sheet_by_name('Sheet2')
    sheet_one1 = workbook.sheet_by_name('Sheet4')
    number = 0
    for j in range(sheet_one1.ncols):
        if str(sheet_one1.cell(0, j).value).find('频率汇总') != -1:
            number = j + 2
    name = []
    cn = []
    for i in range(1, sheet_one.nrows):
        con = []
        name_result = sheet_one.cell(i, 0).value
        name.append(name_result)
        for j in range(1, sheet_one.ncols):
            if sheet_one.cell(i, j).value == '1':
                con.append(j)
        cn.append(con)
    sheet_one = workbook.sheet_by_name('Sheet4')
    content_word = []
    for j in range(number, sheet_one.ncols):
        for i in range(1, sheet_one.nrows):
            result = sheet_one.cell(i, j).value
            if result != '':
                content_word.append(result)
    content1 = [content_word[0]]
    for i in range(len(content_word)):
        result = content_word[i]
        count = 0
        for j in content1:
            if j == result:
                count = count + 1
        if count == 0:
            content1.append(result)
    num = []
    for m in content1:
        cn1 = []
        for j in range(number, sheet_one.ncols):
            for i in range(1, sheet_one.nrows):
                result = sheet_one.cell(i, j).value
                if result != '':
                    if str(result) == m:
                        cn1.append(i)
        num.append(cn1)
    s2 = []
    for i in range(len(num)):
        for j in range(len(cn)):
            count = 0
            for m in num[i]:
                for n in cn[j]:
                    result = sheet_one.cell(m, n).value
                    if result != '':
                        count = count + int(float(result))
            s2.append(count)
    s2 = np.reshape(np.array(s2), (len(content1), len(name)))
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('list')
    sheet1.write(0, 0, 'name')
    for i, line in enumerate(s2.tolist()):
        for j, m in enumerate(line):
            sheet1.write(i + 1, j + 1, m)
    for i, line in enumerate(content1):
        sheet1.write(i + 1, 0, line)
    for i, line in enumerate(name):
        sheet1.write(0, i + 1, line)
    book.save(save_home + '/指标矩阵.xls')
    data_xls = pd.read_excel(save_home + '/指标矩阵.xls', 'list', index_col=0)
    data_xls.to_csv(save_home + '/指标矩阵.csv', encoding='gb18030')
    os.remove(save_home + '/指标矩阵.xls')
