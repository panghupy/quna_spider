# import requests
# from lxml import etree
# import re
# from scrapy import selector
# url = 'https://tuan.qunar.com/vc/index.php?category=all_o'
# response = requests.get(url).text
# import json
#
# with open('1.html', 'w')as f:
#     f.write(response)
# #正则在这！！！！！
# result = re.findall('<script>pageLoader\(({"id":"tuan-list".*?)</script>', response)
# # print(result[0])
# res = result[0][:-2]
# res = re.sub("\'",'\"',res)
# obj = json.loads(res)
# print(obj['html'])
# print(type(obj['html']))
# html_response = obj['html']
# with open('a.html','w')as f:
#     f.write(html_response)
# html = selector.Selector(text=html_response)
# title_list = html.xpath('//div[@class="title"]')
# print(title_list)

import re
url = 'https://tuan.qunar.com/vc/index.php?category=all_r&limit=0%2C30'
res = re.search('category=(.*?)&',url).group(1)
print(res)