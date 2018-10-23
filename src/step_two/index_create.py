# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import xlrd
import docx
from xlwt import Workbook
import os

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def content_read(index_home):
    index_content = []
    name_content = []
    for file_name in os.listdir(index_home):
        file = docx.Document(index_home + file_name)
        for para in file.paragraphs:
            temp_content = para.text
            if temp_content:
                index_content.append(temp_content)
                name_content.append(file_name)
    return index_content, name_content


def index_main(save_home, artificial_table, index_home):
    """
          子函数:生成三级指标表，经过人过处理后的文章内容，写入关键词对应的行中，对应step2、process6
          :param: artificial_table:人过处理二级指标的词频表
          :param: artificial_table_sheet:关键词对应的词频表sheet
          :param: index_home:人工处理后对应的三级指标表
          :param: save_home:生成的二级指标对应文件名表保存路径
          """
    content_index, content_name = content_read(index_home)
    workbook = xlrd.open_workbook(artificial_table)
    sheet_one = workbook.sheet_by_name(workbook.sheet_names()[0])
    number_spare = 0
    number_minor = 0
    for j in range(0, sheet_one.ncols):
        if sheet_one.cell(0, j).value == '次备用词':
            number_spare = j
        if sheet_one.cell(0, j).value == '次高频词':
            number_minor = j
    result = []
    for i in range(1, sheet_one.nrows):
        content = []
        content_temp = []
        content_major = []
        for j in range(number_minor - 1, number_spare):
            temp = sheet_one.cell(i, j).value
            if temp:
                content_temp.append(temp)
        for j in range(0, sheet_one.ncols - number_spare):
            temp = sheet_one.cell(i, number_spare + j).value
            if temp:
                content.append(sheet_one.cell(i, number_spare + j).value)
        content_major.append(sheet_one.cell(i, 0).value)
        result.append([l for l in [content_major, content_temp, content] if len(l) > 0])
    result_ans = []

    for i in range(len(result)):
        for j in result[i][1]:
            for m in result[i][2]:
                for i_index, key in enumerate(content_index):
                    if j in key or j in key:
                        # print([result[i][0][0], i_index, content_name[i_index]])
                        result_ans.append([result[i][0][0], i_index, content_name[i_index]])
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('Sheet1')
    sheet2 = book.add_sheet('人工查看')
    two_content = []
    two_name = []
    data_miss_index = []
    data_miss_name = []
    index_number = []
    for i in result_ans:
        index_number.append(i[1])

        two_content.append(i[0])
        two_name.append(i[2])
    for i in range(len(content_index)):
        if i not in index_number:
            data_miss_index.append(content_index[i])
            data_miss_name.append(content_name[i])  # num = [[row[i] for row in num] for i in range(len(num[0]))]
    sheet1.write(0, 1, '二级指标')
    sheet1.write(0, 0, '文件')
    for i, line in enumerate(two_content):
        sheet1.write(i + 1, 1, line)
    for i, line in enumerate(two_name):
        sheet1.write(i + 1, 0, line)
    sheet2.write(0, 1, '目录')
    sheet2.write(0, 0, '文件')
    for i, line in enumerate(data_miss_index):
        sheet2.write(i + 1, 1, line)
    for i, line in enumerate(data_miss_name):
        sheet2.write(i + 1, 0, line)
    book.save(save_home + '/step_three/二级指标人工处理中.xls')



