import requests
import re

def gethtml(url):
    headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
    html=requests.get(url,headers=headers)
    return html.text
def gettarget(html):
    line=re.compile('<a href="javascript:;">(.*?)</a>')
    target=re.findall(line,html)
    for i in range(target):
        print(i)
