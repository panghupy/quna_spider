# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QunaItem(scrapy.Item):
    # 分类
    djscategory = scrapy.Field()
    # 标题
    djstitle = scrapy.Field()
    # 图片链接
    djsimg_url = scrapy.Field()
    # 出游类型
    djstype_gt = scrapy.Field()
    # 简介
    djsjiejian = scrapy.Field()
    # 价格
    djsprice = scrapy.Field()
    # 参团日期
    djsdate = scrapy.Field()
    # 参团人数
    djsnum = scrapy.Field()
    # 详情链接
    djsdetail_url = scrapy.Field()
    # 项目id
    _id = scrapy.Field()

    def get_collection_name(self):
        return 'djs' + self.get('djscategory')
