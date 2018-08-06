# -*- coding: utf-8 -*-
import scrapy
import re
import json
from scrapy import selector
from quna.items import QunaItem


class QunaSpiderSpider(scrapy.Spider):
    name = 'quna_spider'
    allowed_domains = ['qunar.com']
    start_urls = ['https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30',
                  'https://tuan.qunar.com/vc/index.php?category=all_i&limit=0%2C30',
                  'https://tuan.qunar.com/vc/index.php?category=all_o&limit=0%2C30'
                  ]

    def parse(self, response):
        limit = int(re.search('\d+', response.url).group())

        next_url = re.sub('\d+', str(limit + 30), response.url, count=1)
        yield scrapy.Request(next_url, self.parse)
        result = re.findall('<script>pageLoader\(({"id":"tuan-list".*?)</script>', response.text)
        res = result[0][:-2]
        res = re.sub("\'", '\"', res)
        obj = json.loads(res)
        html_response = obj['html']
        html = selector.Selector(text=html_response)
        li_list = html.xpath('//div[@id="list"]//li')
        for li in li_list:
            item = QunaItem()
            item['djscategory'] = re.search('category=(.*?)&', response.url).group(1)
            item['_id'] = re.search('\d+', li.xpath('./a/@href').extract_first()).group()
            item['djstitle'] = li.xpath('.//div[@class="nm"]/@title').extract_first()
            item['djsimg_url'] = li.xpath('.//div[@class="imgs loading"]/img/@src').extract_first()
            item['djstype_gt'] = li.xpath('.//div[@class="type_gt"]/text()').extract_first()
            item['djsjiejian'] = li.xpath('.//div[@class="sm"]/@title').extract_first()
            item['djsprice'] = li.xpath('.//div[@class="price"]//em/text()').extract_first()
            item['djsdate'] = li.xpath('.//div[@class="tip"]//span[1]/text()').extract_first()
            item['djsnum'] = li.xpath('.//div[@class="tip"]//span[2]/em/text()').extract_first()
            item['djsdetail_url'] = li.xpath('./a/@href').extract_first()
            yield item
