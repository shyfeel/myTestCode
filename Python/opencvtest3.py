# -*- coding: utf-8 -*-
"""
ͼ��ģ��ƥ��
ģ��ƥ������ͼ����Ѱ��Ŀ��ķ���֮һ
ģ��ƥ��Ĺ�����ʽ
 ģ��ƥ��Ĺ�����ʽ��ֱ��ͼ�ķ���ͶӰ����һ�������¹����������ģ�ͨ��������ͼ���ϻ���ͼ����ʵ�ʵ�ͼ��������ͼ�����ƥ�䡣
 ����������һ��100x100������ͼ����һ��10x10��ģ��ͼ�񣬲��ҵĹ����������ģ�
 ��1��������ͼ������Ͻ�(0,0)��ʼ���и�һ��(0,0)��(10,10)����ʱͼ��
 ��2������ʱͼ���ģ��ͼ����жԱȣ��ԱȽ����Ϊc��
 ��3���ԱȽ��c�����ǽ��ͼ��(0,0)��������ֵ��
 ��4���и�����ͼ���(0,1)��(10,11)����ʱͼ�񣬶Աȣ�����¼�����ͼ��
 ��5���ظ���1������4����ֱ������ͼ������½ǡ�
ģ��ƥ���ƥ�䷽ʽ
    ��OpenCv��EmguCv��֧������6�ֶԱȷ�ʽ��
    CV_TM_SQDIFF ƽ����ƥ�䷨���÷�������ƽ����������ƥ�䣻��õ�ƥ��ֵΪ0��ƥ��Խ�ƥ��ֵԽ��
    CV_TM_CCORR ���ƥ�䷨���÷������ó˷���������ֵԽ�����ƥ��̶�Խ�á�
    CV_TM_CCOEFF ���ϵ��ƥ�䷨��1��ʾ������ƥ�䣻-1��ʾ����ƥ�䡣
    CV_TM_SQDIFF_NORMED ��һ��ƽ����ƥ�䷨
    CV_TM_CCORR_NORMED ��һ�����ƥ�䷨
    CV_TM_CCOEFF_NORMED ��һ�����ϵ��ƥ�䷨
�ο���http://www.cnblogs.com/xrwang/archive/2010/02/05/MatchTemplate.html
"""
import cv2
#import numpy as np
#from matplotlib import pyplot as plt

img = cv2.imread('D:\imgtest\screen.jpg',0)
img2 = img.copy()
template = cv2.imread('D:\imgtest\startgame.jpg',0)
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    #min_loc��Сֵλ�ã�max_loc���ֵλ�ã�
    #print min_loc;
    print max_loc;
    print max_loc[0];
    print max_loc[1];
    # print max_val;