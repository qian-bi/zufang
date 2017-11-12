# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class ZufangPipeline(object):

    def open_spider(self, spider):
        print('a')
        self.conn = pymysql.connect(host='localhost',
                                    user='LiaoJiabin',
                                    password='Ljb1993QB',
                                    port=3306,
                                    db='scrapy',
                                    charset='utf8')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        print('b')
        print(spider.name, 'pipelines')
        title = item['title']
        money = item['money']
        insert_sql = 'INSERT INTO zufang values (\'%s\', \'%s\');' % (
            title, money)

        self.cur.execute(insert_sql)
        self.conn.commit()
        # return item

    def spider_close(self, spider):
        print('c')
        self.conn.close()
