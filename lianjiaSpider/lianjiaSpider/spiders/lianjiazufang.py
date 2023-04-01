# -*- coding: utf-8 -*-
import scrapy
from lianjiaSpider.items import LianjiaspiderItem
import re

class LianjiazufangSpider(scrapy.Spider):
    name = 'lianjiazufang'
    allowed_domains = ['lianjia.com']
    start_urls = []
    with open(r'/Users/zhutom/sites/CrawlerProject-master/lianjia_scrapy/url_list.txt', 'r') as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        house_list = response.xpath('//div[@class="content__list"]/div')
        for house in house_list:
            item = LianjiaspiderItem()
            item['title'] = house.xpath('./a[@class="content__list--item--aside"]/@title').extract_first()
            item['link'] = 'https://sh.lianjia.com' + house.xpath('./a[@class="content__list--item--aside"]/@href').extract_first()
            item['location'] = '.'.join(house.xpath('./div/p[2]/a/text()').extract())
            yield scrapy.Request(
                item['link'],
                callback=self.parse_detail,
                meta={'item': item}
            )

    def parse_detail(self, response):
        item = response.meta['item']
        rent = response.xpath('//div[@class="content__aside--title"]/span[1]/text()').extract_first()
        item['rent'] = int(rent)
        # item['apartment_layout'] = ""
        apartment_layout = response.xpath('//ul[@class="content__aside__list"]/li[2]/text()').get()
        item['apartment_layout'] = re.findall('.*(\d室\d厅\d卫).*', apartment_layout)[0]

        # item['area'] = response.xpath('//p[@class="content__article__table"]/span[3]/text()').extract_first()
        floor = response.xpath('//div[@class="content__article__info"]/ul/li[2]').extract_first()
        area = re.findall('.*面积：(.*)㎡</li>', floor)[0]
        item['area'] = float(area)

        # item['orientation'] = response.xpath('//p[@class="content__article__table"]/span[4]/text()').extract_first()
        item['orientation'] = ""
        publish_time = response.xpath('//div[@class="content__subtitle"]/text()').get()
        item['publish_time'] = re.findall('.*房源维护时间：(\d\d\d\d-\d\d-\d\d)', publish_time)[0]
        # item['publish_time'] = ""
        # item['unit_price'] = response.xpath('//p[@class="content__aside--title"]/span/text()').extract_first()
        item['unit_price'] = 0
        
        floor = response.xpath('//div[@class="content__article__info"]/ul/li[8]').extract_first()
        item['floor'] = re.findall('.*楼层：(.*)</li>', floor)[0]
        item['longitude'] = re.findall("longitude: '(.*)',", response.text)[0]
        item['latitude'] = re.findall("latitude: '(.*)'", response.text)[0]
        yield item
        