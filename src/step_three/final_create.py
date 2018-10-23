# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:21:28 2018

@author: bob.lee
"""
import os
import pandas as pd
import numpy as np
from xlwt import Workbook

DATA_HOME = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'temp/'))
if not os.path.isdir(DATA_HOME):
    os.mkdir(DATA_HOME)


def weights_create(csv_name, save_home):
    book = Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('等同权重')
    sheet2 = book.add_sheet('加权权重')
    f = open(csv_name)
    res = pd.read_csv(f)
    level_two = []
    level_two_name = []
    level_three_name = []
    data = np.array(res.loc[:, :])
    row_, cols = data.shape
    for i, rows in enumerate(res):
        if rows != 'name':
            level_two_name.append(rows)
            level_two.append(sum(res[rows]))
    same_content = []
    frequency_content = []
    for m, line in enumerate(data):
        content_line = []
        level_three_name.append(line[0])
        for v, j in enumerate(line):
            if v != 0:
                if level_two[v - 1] != 0:
                    content_line.append(j / level_two[v - 1])
                    frequency_content.append(1 / (cols - 1))
                else:
                    content_line.append(0)
                    frequency_content.append(1 / (cols - 1))
        same_content.append(content_line)
    s2 = np.reshape(np.array(same_content), (cols - 1, row_))
    sheet1.write(0, 0, 'name')
    for i, line in enumerate(s2.tolist()):
        for j, m in enumerate(line):
            sheet1.write(i + 1, j + 1, m)
    for i, line in enumerate(level_two_name):
        sheet1.write(i + 1, 0, line)
    for i, line in enumerate(level_three_name):
        sheet1.write(0, i + 1, line)
    s2 = np.reshape(np.array(frequency_content), (cols - 1, row_))
    sheet2.write(0, 0, 'name')
    for i, line in enumerate(s2.tolist()):
        for j, m in enumerate(line):
            sheet2.write(i + 1, j + 1, m)
    for i, line in enumerate(level_two_name):
        sheet2.write(i + 1, 0, line)
    for i, line in enumerate(level_three_name):
        sheet2.write(0, i + 1, line)
    book.save(save_home + '/weight.xls')


def visual_cluster(csv_home, save_home):
    """
      子函数:生成ratio矩阵、heatmap图，对应step5,6,7 需安装r语言
      :param: csv_home:二三级关系矩阵
      :param: ratio_home:ratio矩阵的保存路径
      :param: heatmap_home:heatmap热力图的保存路径
      :param: level_three_home:三级指标聚类图的保存路径
      :param: level_two_home:二级指标聚类图的保存路径
      """
    weights_create(csv_home, save_home)
    location = os.path.join(os.path.dirname(__file__))
    ratio_home = save_home + '/da_ratio.csv'
    heatmap_home = save_home + '/heat_map.pdf'
    level_two_home = save_home + '/level_two_cluster.pdf'
    level_three_home = save_home + '/level_three_cluster.pdf'
    ans = 'Rscript ' + location + '/code.R ' + location + ' ' + csv_home + ' ' + ratio_home + ' ' + heatmap_home + ' ' \
          + level_three_home + ' ' + level_two_home
    os.system(ans)
