# 爬虫的说明文档

乐岸教育教学辅助项目。

scrapy的使用方式：

    scrapy list
    scrapy crawl domz
    scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"

最简单的存储爬虫数据的方式：

    scrapy crawl dmoz -o items.json

将抓取到的数据存储到MySQL中，首先，在MySQL的test库下新建一张表：

    create table resources(id int auto_increment primary key, title varchar(100), link varchar(100), `desc` blob)engine=innodb;

然后，在settings.py中，进行简单的配置，并在pipeline.py中实现相应的逻辑。

存放豆瓣图书的建表语句：

    create table douban_books(`id` int auto_increment primary key, `title` blob, `link` varchar(100), `desc` blob, `detail` blob)engine=innodb;
