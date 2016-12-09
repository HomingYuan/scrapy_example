# -*- coding: utf-8 -*-
from __future__ import print_function

import scrapy
from scrapy_example.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="title-and-desc"]'):
            item  = DmozItem()
            item['title'] = sel.xpath('./a/div/text()').extract()[0] # 标题
            item['link']  = sel.xpath('./a/@href').extract()[0] # 链接
            item['desc']  = sel.xpath('./div/text()').extract()[0].strip() # 详细描述
            yield item
