#coding=utf-8
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import random
import requests
import pandas as pd
import numpy as np
def getURL(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
    html = requests.get(url, headers=headers)
    html.encoding='gbk'
    return html.text
def gettarget(html):
    data=[]
    i=0
    target=re.compile('<img src="(.*?)\.jpg">')
    targetlist=re.findall(target,html)
    for i in targetlist:
        data.append(i)
    return data
target=[]
for i in range (1,265):
    url='https://search.51job.com/list/080200,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,'+str(i)+'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    content=getURL(url)
    target.append(gettarget(content))
print(target)
target.to_csv('e:/1.csv',encoding='utf_8_sig')



