# 向数据库中请求网址的后四位字符,抓取网站内容,并修改数据库中的spider状态为"Done"
import pymongo

from spiders import pages_details

from urlids import get_url_id

client = pymongo.MongoClient('localhost',27017)
javmoo = client['javmoo']
movie_details = javmoo['movie_details']
url_ids = javmoo['url_ids']
url_ids_done = javmoo['url_ids_done']
#通过输入最新的番号来确定抓取网址的4位字符

get_url_id('5eex')


db_id = [item['id'] for item in url_ids.find()]
for i in db_id:
    header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    url = 'http://www.avmoo.net/cn/movie/' + i
    pages_details(url,i)

print('done')
