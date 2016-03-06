# 向数据库中请求网址的后四位字符,抓取网站内容,并修改数据库中的spider状态为"Done"
from bs4 import BeautifulSoup
import requests
import time
import re
import pymongo

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
url = 'http://www.avmoo.net/cn'
web_data = requests.get(url,header)
time.sleep(2)
Soup = BeautifulSoup(web_data.text,'lxml')
