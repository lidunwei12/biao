# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import xlrd
from xlwt import Workbook
import os

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def content_check_main(data_home, data_handle_home, save_home):
    """
      子函数:生成三级指标表，经过人过处理后的文章内容，写入关键词对应的行中，对应step2、process6
      :param: data_home:关键词对应的词频表
      :param: data_sheet:关键词对应的词频表sheet
      :param: data_handle_home:人工处理后对应的三级指标表
      :param: data_handle_sheet:人工处理后对应的三级指标表sheet
      :param: save_home:生成的三级指标保存路径
      """
    workbook = xlrd.open_workbook(data_home)
    sheet_one = workbook.sheet_by_name(workbook.sheet_names()[0])
    content_word = []
    for i in range(1, sheet_one.nrows):
        result = sheet_one.cell(i, 0).value
        if result:
            content_word.append(result)
    print(len(content_word))
    workbook1 = xlrd.open_workbook(data_handle_home)
    sheet_one1 = workbook1.sheet_by_name(workbook1.sheet_names()[0])
    result_content = []
    for i in range(len(content_word)):
        result_temp = []
        for j in range(1, sheet_one1.nrows):
            result = str(sheet_one1.cell(j, 0).value)
            result = result[0:result.find(' ')]
            if result == content_word[i]:
                result_temp.append(sheet_one1.cell(j, 1).value)
        result_content.append(result_temp)
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('list')
    try:
        for i, line in enumerate(result_content):
            print(len(line))
            if len(line) > 256:
                line = line[0:255]
            for j, m in enumerate(line):
                sheet1.write(i + 1, j + 1, m)
        for i, line in enumerate(content_word):
            sheet1.write(i + 1, 0, line)
        book.save(save_home + '/三级指标.xls')
        print(len(result_content))
    except ValueError as e:
        print(e)



