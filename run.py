#导入相关库
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
#设置页面页的可变部分
page=('pg')
#设置请求头部信息
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://www.baidu.com/link?url=_andhfsjjjKRgEWkj7i9cFmYYGsisrnm2A-TN3XZDQXxvGsM9k9ZZSnikW2Yds4s&amp;amp;wd=&amp;amp;eqid=c3435a7d00006bd600000003582bfd1f'
}
def main():
    #设置列表页URL的固定部分
    url='https://bj.lianjia.com/ershoufang/'
    a=(url+page+'/')
    r=requests.get(url=a,headers=headers)
    html=r.content
    #解析抓取的页面内容
    lj=BeautifulSoup(html,'html.parser')
    positionInfo=lj.find_all('div',attrs={'class':'section_sub_nav'})
    #print(return_regin(positionInfo))
    positionInfo = return_regin(positionInfo)
    #print(positionInfo)
    for regin in positionInfo:
        regin1 =regin
        url1 = url+regin
        Crawling_data(url1,is_sellect(regin),regin1)
    pass 
#Crawling_data(url,positionInfo)
#h获取北京各个区
def return_regin(positionInfo):
    #h获取各区域
    a_lis = []
    for item in positionInfo:
         pzzr=item.find_all('a')
         #print(pzzr)
         for item in pzzr:
             a_lis.append(item.get("href").split('/')[-2])
    a_lis.pop()
    return a_lis  
    pass
#判断当前选择的区
def is_sellect(regin):
    url='https://bj.lianjia.com/ershoufang/'+regin+'/'
    a=(url+page+'/')
    r=requests.get(url=a,headers=headers)
    html=r.content
    #解析抓取的页面内容
    lj=BeautifulSoup(html,'html.parser')
    positionInfo=lj.find_all('div',attrs={'class':'section_sub_nav'})
    #h获取各区域
    for item in positionInfo:
         pzzr=item.find_all('a')
         #print(pzzr)
         for item in pzzr:
             link = item.get('class')
             #判断如果是该区则返回
             if link:
                 return item.string
    pass
#判定数字 
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False  
def Crawling_data(url1,regin,regin1):
    #循环抓取列表页信息
    for i in range(1,10):
         if i == 1:
             i=str(i)
             a=(url1+'/'+page+i+'/')
             r=requests.get(url=a,headers=headers)
             html=r.content
         else:
             i=str(i)                
             a=(url1+'/'+page+i+'/')
             r=requests.get(url=a,headers=headers)
             html2=r.content
             html = html + html2
         #每次间隔1秒
         time.sleep(0.5)
    #解析抓取的页面内容
    lj=BeautifulSoup(html,'html.parser')
    #提取房源总价
    price=lj.find_all('div',attrs={'class':'priceInfo'})
    tp=[]
    re = []
    for a in price:
        totalPrice=a.span.string
        #print(totalPrice)
        tp.append(totalPrice)
        re.append(regin)
    #提取房源信息
    houseInfo=lj.find_all('div',attrs={'class':'houseInfo'})   
    #hi=[]
    xiaoqu = []
    huxing = []
    mianji = []
    chaoxiang = []
    zhuangxiu = []
    dianti = []
    l = []
    for b in houseInfo:
        house=b.get_text()
        #数据清洗
        l = house.split('/')
        #print(l[1].split('室')[0])
        if len(l)==7:
            del l[1]
        if len(l)==6 and not (is_number(l[1].split('室')[0])):
            del l[1]
        if len(l)==5:
            l.append('无电梯')
        #hi.append(house)
        #print(l)
        xiaoqu.append(l[0])
        huxing.append(l[1])
        mianji.append(float(l[2].split('平米')[0]))
        chaoxiang.append(l[3])
        zhuangxiu.append(l[4])
        dianti.append(l[5])
    #提取房源关注度
    followInfo=lj.find_all('div',attrs={'class':'followInfo'})
    guanzhu=[]
    daikan=[]
    unitprice = []      
    for c in followInfo:
        follow=c.get_text()
        if len(follow.split('/'))!=3:
            print(follow.split('/'))
        #print(len(follow.split('/'))!=3)
        guanzhu.append(int(follow.split('/')[0].split('人关注')[0]))
        daikan.append(int(follow.split('/')[1].split('次带看')[0]))
        #fi.append(follow)
        unitprice.append(int(follow.split('/')[1].split('单价')[1].split('元')[0]))
    #创建数据表
    house=pd.DataFrame({'region':re,'totalprice':tp,'unitprice':unitprice,'xiaoqu':xiaoqu,'huxing':huxing,'mianji':mianji,'chaoxiang':chaoxiang,'zhuangxiu':zhuangxiu,'dianti':dianti,'guanzhu':guanzhu,'daikan':daikan})
    print(len(house))
    if len(house):
        house.to_csv("lianjiawang"+regin1+".csv",encoding="GBK")
    pass
if __name__ == '__main__':
    main()