# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
from src.data_prepare.pattern_to_docx import prepare_docx
import re
import jieba.analyse as analyse
import numpy as np
from xlwt import Workbook
from zipfile import ZipFile
from bs4 import BeautifulSoup
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def word_choose(file_name):
    """
    子函数:思路，将word内容转化成zip ，并提取内容和jiebe分词
    :param: file_name:word 文件名
    :return: 文件内容
    :return: 分词结果
    """
    content = []
    content_result = []
    try:
        document = ZipFile(file_name)
        xml = document.read("word/document.xml")
        word_obj = BeautifulSoup(xml.decode("utf-8"))
        texts = word_obj.findAll("w:t")
        for text in texts:
            content_result.append(text.text)
            temp = analyse.extract_tags(text.text, withWeight=False, allowPOS=())
            content.extend(temp)
    except Exception as e:
        print(e)
    return content, content_result


def file_word_choose(file_dir):
    """
    子函数:思路，提取文件夹中word和分词结果，汇总成词频的词语
    :param: file_dir:word 文件夹
    :return: 汇总分词结果
    """
    result = []
    for file in os.listdir(file_dir):
        temp, _ = word_choose(file_dir + file)
        temp = list(set(temp))
        if temp:
            result.extend(temp)
    return list(set(result))


def catalogue_word_frequency(file_dir, save_home, save_name, sheet_name):
    """
    子函数:思路：首先创建一张字典，里面的key是分词的词语，value是初始化0，遍历文件，每一个文件正则提取key，并修改value
    :param: file_dir:word 文件夹
    :param: save_home:词频表的保存路径
    :param: save_home:词频表的保存名字
    """
    num = []
    file_name = []
    word_result = file_word_choose(file_dir)
    word_dict = {}
    for word_content in word_result:
        word_value = 0
        word_dict[word_content] = word_value
    for word_file in os.listdir(file_dir):
        print(word_file)
        file_name.append(word_file)
        _, content_temp = word_choose(file_dir + word_file)
        for key, value in word_dict.items():
            ans_temp = 0
            if content_temp:
                for i in content_temp:
                    ans_temp = ans_temp + len(re.findall(key, i))
            word_dict[key] = ans_temp
        value_temp = list(word_dict.values())
        num.append(value_temp)
        for key, value in word_dict.items():
            word_dict[key] = 0
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet(sheet_name)
    word_content1 = []
    word_content_temp = list(word_dict.keys())
    for key in word_content_temp:
        word_content1.append(key)
    num = [[row[i] for row in num] for i in range(len(num[0]))]
    s2 = np.reshape(np.array(num), (len(word_result), len(file_name)))
    for i, line in enumerate(s2.tolist()):
        for j, m in enumerate(line):
            sheet1.write(i + 1, j + 1, m)
    for i, line in enumerate(word_content1):
        sheet1.write(i + 1, 0, line)
    for i, line in enumerate(file_name):
        sheet1.write(0, i + 1, line)
    book.save(save_home + save_name)
    return '分词表创建成功'


def prepare_main(prepare_id, content_file, catalog_file):
    status = 1
    temp_home = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/' + str(prepare_id)))
    if not os.path.isdir(temp_home):
        os.mkdir(temp_home)
    home = ['content/', 'index/', 'step_one/', 'step_two/', 'step_three/']
    for s in home:
        make_home = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/' + str(prepare_id) + '/' + s))
        if not os.path.isdir(make_home):
            os.mkdir(make_home)
    try:
        prepare_docx(prepare_id, content_file, catalog_file)
        catalogue_word_frequency(DATA_HOME + '/' + str(prepare_id) + '/content/',
                                 DATA_HOME + '/' + str(prepare_id) + '/step_one',
                                 '/内容分词结果.xls',
                                 '内容分词')
        catalogue_word_frequency(DATA_HOME + '/' + str(prepare_id) + '/index/',
                                 DATA_HOME + '/' + str(prepare_id) + '/step_one',
                                 '/目录分词结果.xls', '目录分词')
        return {
            'prepare_id': prepare_id,
            'prepare_status': status,
            'content_frequency': DATA_HOME + '/' + str(prepare_id) + '/step_one/内容分词结果.xls',
            'catalog_frequency': DATA_HOME + '/' + str(prepare_id) + '/step_one/目录分词结果.xls'
        }
    except:
        status = 0
        return {
            'prepare_id': prepare_id,
            'prepare_status': status,
            'content_frequency': '',
            'catalog_frequency': ''
        }
