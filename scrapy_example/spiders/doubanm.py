# -*- coding: utf-8 -*-
import scrapy
from scrapy_example.items import DoubanMItem


class DoubanmSpider(scrapy.Spider):
    name = "doubanm"
    start_urls = ['https://movie.douban.com/top250/']

    def parse(self, response):
        item = DoubanMItem()
        for sel in response.xpath('//*[@id="content"]/div/div[1]//li'):

            item['title'] = sel.xpath('.//span/text()')[0].extract()
            item['detail_url'] = sel.xpath('.//a/@href')[0].extract()
            item['image_url'] = sel.xpath('.//img/@src')[0].extract()
            item['rank'] = sel.xpath('.//*[@class="rating_num"]/text()').extract()[0]
            item['detail'] = sel.xpath('.//p/text()').extract()[0].strip()
            yield item

        try:
            next_page = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/link/@href').extract()[0]
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        except:
            pass
