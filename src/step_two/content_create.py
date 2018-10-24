# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import docx
import re
import xlrd
import os
from xlwt import Workbook

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def content_main(file_home, classifier_home, key_word_home, save_home):
    """
          子函数:三级指标与词汇匹配，，对应step2、process1-4
          :param: file_home:政策文件所存放的路径
          :param: classifier_home:量词表
          :param: classifier_sheet:量词表对应的表名
          :param:  key_word_home:内容关键词对应的词频表
          :param: save_home:三级指标人工处理表所存放的路径
          """
    # print(len([name for name in os.listdir(DATA_HOME + '/content') if
    #            os.path.isfile(os.path.join(DATA_HOME + '/content', name))]))
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('list')
    sheet1.write(0, 0, '关键词+量词')
    sheet1.write(0, 1, '句子')
    ans_line = 0
    content_liang = []
    liang_no = []
    no_number = []
    workbook_liang = xlrd.open_workbook(classifier_home)
    classifier_sheet = workbook_liang.sheet_names()[0]
    sheet_liang = workbook_liang.sheet_by_name(classifier_sheet)
    for j in range(sheet_liang.ncols):
        if sheet_liang.cell(0, j).value == '量词':
            for i in range(1, sheet_liang.nrows):
                content_liang.append(sheet_liang.cell(i, j).value)
        if sheet_liang.cell(0, j).value == '不包含':
            for i in range(1, sheet_liang.nrows):
                temp = sheet_liang.cell(i, j).value
                liang_no.append(temp.split('、'))
                if temp:
                    no_number.append(i - 1)
    workbook = xlrd.open_workbook(key_word_home)
    sheet_one_content = workbook.sheet_by_name('内容分词')
    content_word = []
    for i in range(1, sheet_one_content.nrows):
        result = sheet_one_content.cell(i, 0).value
        if result:
            content_word.append(result)
    for file in os.listdir(file_home):
        try:
            print(file)
            if file.find('pdf') == -1:
                content = []
                if file.find('~$') != -1:
                    continue
                file = docx.Document(file_home + file)
                for para in file.paragraphs:
                    content.append(para.text)
                result = ''.join(content)
                rr = re.compile(r'，|。|！|？|；', re.I)  # 不区分大小写
                match = re.split(rr, result)
                result_key = []
                result_content = []
                # print(len(content_word),len(match),len(content_liang))
                for i in range(len(content_word)):
                    for j in range(len(match)):
                        for m in range(len(content_liang)):
                            temp_ans = match[j].find(content_word[i])
                            ans_temp = match[j].find(content_liang[m])
                            if temp_ans != -1 and ans_temp != -1:
                                if temp_ans < ans_temp:
                                    if content_word[i].find(content_liang[m]) != -1:
                                        if len(re.findall(re.compile(content_liang[m]), match[j])) > 1:
                                            if m in no_number:
                                                temp = liang_no[no_number[no_number.index(m)]]
                                                if content_word[i] not in temp:
                                                    result_key.append(content_word[i] + ' ' + content_liang[m])
                                                    result_content.append(match[j])
                                            else:
                                                result_key.append(content_word[i] + ' ' + content_liang[m])
                                                result_content.append(match[j])
                                    else:
                                        if m in no_number:
                                            temp = liang_no[no_number[no_number.index(m)]]
                                            if content_word[i] not in temp:
                                                result_key.append(content_word[i] + ' ' + content_liang[m])
                                                result_content.append(match[j])
                                        else:
                                            result_key.append(content_word[i] + ' ' + content_liang[m])
                                            result_content.append(match[j])
                for i, line in enumerate(result_key):
                    sheet1.write(ans_line + i + 1, 0, line)
                for i, line in enumerate(result_content):
                    sheet1.write(ans_line + i + 1, 1, line)
                ans_line = ans_line + len(result_key)
        except Exception as e:
            pass
    book.save(save_home + '/三级指标人工修正表.xls')


# content_main(DATA_HOME + '/1' +  '/content/', r'C:\Users\yry\Documents\WeChat Files\wxid_gp6l5oft4qci42\Files\量词库.xls',
#              DATA_HOME + '/1' + '/step_one/内容分词结果.xls',
#              DATA_HOME + '/1' + '/step_two')
