#coding=utf-8
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import random
import requests
import pandas as pd
import numpy as np
def getURL(url):
    headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
    html = requests.get(url, headers=headers)
    html.encoding='gbk'
    return html.text
def gettarget(html):
    data=[]
    target=re.compile('"hoverURL":"(.*?)\.jpg"')
    targetlist=re.findall(target,html)
    tmp=0
    for i in targetlist:
        tmp+=1
        urllib.request.urlretrieve(i,'e:/img%s.jpg'%tmp)
    return targetlist
url='http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%98%9F%E6%88%98&ct=201326592&lm=-1&v=flip'
content=getURL(url)
target1=gettarget(content)
print(target)
