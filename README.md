## Quick Start
### 0. install packages
```
pip3 install scrapy pymysql lxml requests
```
### 1. run sql to create table
```
python3 creat_table.py
# WARNING: you may change settings like: host / username / password in this file
```

### 2. get url list
```
python3 get_url_list.py
# TIPS: this will save start urls into url_list.txt, for scrapy to fetch
# WARNING: you may change settings like: price range / bedrooms / if having elevator in this file
```
### 3. run scrapy
```
cd lianjiaSpider
python3 -m scrapy crawl lianjiazufang
# WARNING: you may change settings like: MYSQL_USER / MYSQL_PASSWORD in settings.py file before you start
```

### 4. see logs
```
tail -f lianjiaSpider/scrapy.log
```

![MySQL效果图](https://raw.githubusercontent.com/tommyyz/lianjia_scrapy/main/imgs/mysql.png)