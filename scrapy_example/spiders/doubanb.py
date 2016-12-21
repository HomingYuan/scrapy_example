# -*- coding: utf-8 -*-
import scrapy

from scrapy_example.items import DoubanBItem

class DoubanbSpider(scrapy.Spider):
    name = "doubanb"
    start_urls = ['https://book.douban.com/top250/']

    def parse(self, response):
        for sel in response.xpath('//tr[@class="item"]'):
            item = DoubanBItem()
            item['link']   = sel.xpath('./td[2]/div[1]/a/@href').extract()[0]
            item['title']  = sel.xpath('./td[2]/div[1]/a/@title').extract()[0]
            item['detail'] = sel.xpath('./td[2]/p/text()').extract()[0]
            try:
                item['desc']   = sel.xpath('./td[2]/p/span/text()').extract()[0]
            except:
                item['desc'] = ''
            yield item

        try:
            next_url = response.xpath('//*[@id="content"]/div/div[1]/div/div/span[3]/a/@href').extract()[0]
            yield scrapy.Request(next_url, self.parse)
        except:
            pass
