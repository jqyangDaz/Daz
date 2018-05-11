from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import random
import requests
import pandas as pd
import numpy as np
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
'''
def getTitle(url):
    try:
        html=urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bs0bj=BeautifulSoup(html.read())
        title=bs0bj.body.h1
    except AttributeError as e:
        return None
    return title
title=getTitle('http://www.pythonscraping.com/pages/page1.html')
if title==None:
    print("Title can not be found")
else:
    print(title)
'''
nameList=[]
linkList=[]
directorList=[]
actorList=[]
timeList=[]
countryList=[]
starList=[]
for page in range(10):
    a=page*25
    url='https://movie.douban.com/top250?start='+str(a)+'&filter='
    html=requests.get(url,headers=headers)
    content=html.text
    name = re.compile(r'<span class="title">(.*)</span>')
    movienames = re.findall(name, content)
    for moviename in movienames:
        if 'nbsp' not in moviename:
            nameList.append(moviename)
        else:
            pass
    link=re.compile(r'<a href="(.*)" class="">')
    movielinks=re.findall(link,content)
    for movielink in movielinks:
        linkList.append(movielink)
    director = re.compile(r'导演: (.*)&nbsp;&nbsp;&nbsp;')
    directors = re.findall(director, content)
    for movieDirector in directors:
        directorList.append(movieDirector)
    actor=re.compile(u'主演:(.*)<br>')
    actors=re.findall(actor,content)
    for actorname in actors:
        actorList.append(actorname)
    time=re.compile(r'(\d\d\d\d)&nbsp;/&nbsp;')
    times=re.findall(time,content)
    for movietime in times:
        timeList.append(movietime)
    country=re.compile(r'&nbsp;/&nbsp;(.*)&nbsp;/&nbsp;')
    countrys=re.findall(country,content)
    for countryname in countrys:
        countryList.append(countryname)
    star=re.compile(r'<span class="rating_num" property="v:average">([0-9]+\.[0-9]+)</span>')
    stars=re.findall(star,content)
    for starnum in stars:
        starList.append(starnum)
data=pd.DataFrame({"Names":nameList,"Country":countryList,"Scores":starList ,"Links":linkList})
print(data)
data.to_csv('e:/1.csv',encoding='utf_8_sig')
'''
print(len(nameList))
print(len(directorList))
print(len(actorList))
print(len(timeList))
print(len(countryList))
print(len(starList))
print(len(linkList))
'''





