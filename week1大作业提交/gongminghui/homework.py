import requests
from bs4 import BeautifulSoup
import time

def item_info_zones(url_into):#构建一个函数，获得区域信息
    wb_data=requests.get(url_into)
    soup=BeautifulSoup(wb_data.text,'lxml')
    if len(soup.select('span.c_25d > a'))==2:#用长度判断地区
        zones=soup.select('span.c_25d > a')[0].text+soup.select('span.c_25d > a')[1].text
    elif len(soup.select('span.c_25d > a'))==1:
        zones=soup.select('span.c_25d > a')[0].text
    else:
        zones=str(soup.select('div.breadCrumb.f12 > span > a')[2].text)[0:2]
    return zones

def item_info(url_into):#构建一个函数，获得目标信息
    wb_data=requests.get(url_into)
    soup=BeautifulSoup(wb_data.text,'lxml')
    title=soup.select('h1')[0].text
    views=soup.select('li.count > em')[0].text#这里58做了反爬取，网页端和手机端都抓了一次，都没抓到这个数据
    post_times=soup.select('li.time')[0].text
    prices=soup.select('div.su_con > span')[0].text
    seller_types=u'个人' if soup.select('span.red')[1].text.lstrip()=='' else u'商家'
    zones=item_info_zones(url_into)#调用区域函数，获得区域信息
    cates=soup.select('div.breadCrumb.f12 > span > a')[2].text
    print(u'标题: %s, 浏览量: %s, 发帖时间: %s, 价格: %s元, 卖家类型: %s, 区域: %s, 类目: %s' %
    (title,views,post_times,prices,seller_types,zones,cates))#信息整合
    time.sleep(1)#延时，防反爬

start_url = 'http://bj.58.com/pbdn/?PGTID=0d100000-0000-1121-f41b-137aeef068b7&ClickID=6'#商品目录页
resp = requests.get(start_url)
content = resp.text
soup = BeautifulSoup(content, 'lxml')
num=len(soup.select('td.img > a'))

for i in range(0,num):
    href_url = soup.select('td.img > a')[i].get('href')#从目录页获取到单个商品的地址
    item_info(href_url)#调用函数获得对应商品的信息





