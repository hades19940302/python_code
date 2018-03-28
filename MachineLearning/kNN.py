#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/3/28 15:25

from numpy import *


def creatDataSet():
    group = [['1.0','1.1'],['1.0','1.0'],['0','0'],['0','0.1']]
    labels = ['A','A','B','B']
    return group,labels


def classify0(inX,dataSet,labes,k):
    dataSetSize = dataSet.shape[0]
