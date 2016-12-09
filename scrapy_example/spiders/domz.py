# -*- coding: utf-8 -*-
import scrapy


class DomzSpider(scrapy.Spider):
    name = "domz"
    allowed_domains = ["domz.org"]
    start_urls = ['http://domz.org/']

    def parse(self, response):
        pass
