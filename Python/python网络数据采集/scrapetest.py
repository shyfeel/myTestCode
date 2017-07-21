#-*- coding: UTF-8 -*-
#python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
#html = urlopen("http://www.shyfeel.com")
html = urlopen("http://www.baidu.com")
bsObj = BeautifulSoup(html.read(),"html5lib")
#print(bsObj.a)
liList = bsObj.findAll("li")
for a in liList:
    print(a.get_text())#get_text获取标签内容