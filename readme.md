# 爬虫的说明文档

乐岸教育教学辅助项目。

scrapy的使用方式：

    scrapy list
    scrapy crawl domz
    scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"

最简单的存储爬虫数据的方式：

    scrapy crawl dmoz -o items.json
