from bs4 import BeautifulSoup
d=[]
path='F:/python/spider/week1/1_2/1_2code_of_video/web/new_index.html'
with open(path,'r')as wb_data:
    Soup=BeautifulSoup(wb_data.read(),'lxml')
    images=Soup.select('body > div.main-content > ul > li > img')
    titles=Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    rates=Soup.select('body > div.main-content > ul > li > div.rate > span')
    cates=Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info ')
    descs=Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
for title,image,rate,cate,desc in zip(titles,images,rates,cates,descs):
    data={
        'title':title.get_text(),
        'image':image.get('src'),
        'rate':rate.get_text(),
        'cate':list(cate.stripped_strings),
        'desc':desc.get_text()

    }
    d.append(data)
for i in d:
    if float(i['rate'])>3:
        print(i['title'])