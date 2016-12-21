# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from __future__ import unicode_literals
import  pymysql


from scrapy_example import settings


class DmozPipeline(object):

    def __init__(self):
        self.connection = pymysql.connect(host=settings.MYSQL_HOST,
                port=settings.MYSQL_PORT,
                user=settings.MYSQL_USER,
                passwd=settings.MYSQL_PASSWORD,
                db=settings.MYSQL_DB)

    def close_spider(self, spider):
        if hasattr(self, 'connection'):
            self.connection.close()

    def process_item(self, item, spider):
        with self.connection as cur:
            #create table resources(id int auto_increment primary key, title varchar(100), link varchar(100), `desc` blob)engine=innodb;
            sql = """insert into resources(`title`, `link`, `desc`) values("{0}", "{1}", "{2}")""".format(item['title'], item['link'], item['desc'])
            cur.execute(sql)


class DoubanBPipeline(object):

    def __init__(self):
        self.connection = pymysql.connect(host=settings.MYSQL_HOST,
                port=settings.MYSQL_PORT,
                user=settings.MYSQL_USER,
                passwd=settings.MYSQL_PASSWORD,
                db=settings.MYSQL_DB)

    def close_spider(self, spider):
        if hasattr(self, 'connection'):
            self.connection.close()

    def process_item(self, item, spider):
        with self.connection as cur:
            sql = """insert into douban_books(`title`, `link`, `desc`, `detail`)
                    values("{0}", "{1}", "{2}", "{3}")""".format(item['title'],
                    item['link'], item['desc'], item['detail'])
            cur.execute(sql.encode('utf-8'))
