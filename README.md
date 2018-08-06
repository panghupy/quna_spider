# quna_spider
此项目的功能是爬取去哪儿网团购模块的信息，爬虫框架使用scrapy，数据存储使用mongo,纯属学习scrapy框架的产物。
此项目中，需要获取的数据在html中的<script></script>标签中，所以需要用正则来提取。
## 特殊说明：
由于本人对scrapy框架中的下载中间件不熟练，所以没有下载图片
## 文件说明
- djsqnw 此文件夹为mongo数据库备份文件
- quna/quna/spiders/quna_spider.py 爬虫文件
- quna/下其余文件为项目部署文件


## 基本概况
抓取字段：分类、标题、图片链接、出游类型、简介、价格、参团日期、参团人数、详情链接、项目id(唯一id，可用于继续获取其他数据。)

## 项目部署
这里使用[scrapyd](https://scrapyd.readthedocs.io/en/latest/)进行项目部署
部署命令：
```
scrapyd-deploy -p quna
```
