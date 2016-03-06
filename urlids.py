import pymongo
client = pymongo.MongoClient('localhost',27017)
javmoo = client['javmoo']
url_ids = javmoo['url_ids']
# 3-6日 最新的片子番号
new_id = '5e9f'
ALL_URL_IDS = []
movie_id1 = ["0","1","2","3","4","5"]
movie_id2 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
movie_id3 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
movie_id4 = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for a in movie_id1:
    url_id = a
    for b in movie_id2:
        url_id1 = url_id+b
        for c in movie_id3:
            url_id2 = url_id1+c
            for d in movie_id4:
                url_id3 = url_id2+d
                ALL_URL_IDS.append(url_id3)
e = ALL_URL_IDS.index(new_id)+1
url_id_now = ALL_URL_IDS[0:e]
url_id_now.reverse()
d = len(url_id_now)


for i in url_id_now:
    data={
        "id":i,
        "spider":"None"
    }
    url_ids.insert_one(data)
    print(i+'写入完成')
print("完成抓取网页ID写入")
