# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os
import xlrd
from xlwt import Workbook
import numpy as np

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def level_two_handle(index_home, level_two_home, save_home):
    """
          子函数:生成二级指标表，经过人过处理后的政策文件名，写入二级指标对应的行中，对应step3、process4
          :param: index_home:政策目录文件路径
          :param: level_two_home:人工处理二级指标表路径
          :param: level_two_sheet:人工处理二级指标表sheet
          :param: save_home:生成的二级指标保存路径
          """
    file_name = []
    for file in os.listdir(index_home):
        if file.find('~$') != -1:
            continue
        file = file[0:file.find('.')]
        # print(file)
        file_name.append(file)
    workbook = xlrd.open_workbook(level_two_home)
    sheet_one = workbook.sheet_by_name(workbook.sheet_names()[0])
    word_cols = 0
    word_content = 0
    for i in range(0, sheet_one.ncols):
        result = sheet_one.cell(0, i).value
        if result.find('二级指标') != -1:
            word_cols = i
        if result.find('文件') != -1:
            word_content = i
    content_level_two = []
    for i in range(1, sheet_one.nrows):
        result = sheet_one.cell(i, word_cols).value
        if result not in content_level_two:
            content_level_two.append(result)
    print(content_level_two)
    level_two_file = []
    for i in range(len(content_level_two)):
        ans = []
        for j in range(1, sheet_one.nrows):
            if sheet_one.cell(j, word_cols).value == content_level_two[i]:
                data1 = sheet_one.cell(j, word_content).value
                ans.append(data1[0:data1.find('.')])
        level_two_file.append(ans)
    content = []
    print(file_name)
    print(level_two_file)
    for i in range(len(level_two_file)):
        temp = []
        for j in range(len(file_name)):
            if file_name[j] in level_two_file[i]:
                temp.append('1')
            else:
                temp.append(' ')
        content.append(temp)
    content = np.reshape(np.array(content), (len(content_level_two), len(file_name)))
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('list')
    sheet1.write(0, 0, 'name')
    for i, line in enumerate(content.tolist()):
        for j, m in enumerate(line):
            sheet1.write(i + 1, j + 1, m)
    for i, line in enumerate(file_name):
        sheet1.write(0, i + 1, line)
    for i, line in enumerate(content_level_two):
        sheet1.write(i + 1, 0, line)
    book.save(save_home + '/二级指标.xls')



