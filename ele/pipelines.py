# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from ele.pymysqlpool import ConnectionPool
from ele import settings


class EleMysqlPipeline(object):

    def __init__(self):
        config = dict(
            pool_name='eleshop',
            host=settings.MYSQL_HOST,  # 读取settings中的配置
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWD,
            database=settings.MYSQL_DBNAME,
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
        )
        self.pool = ConnectionPool(**config)

    def process_item(self, item, spider):
        with self.pool.cursor() as cursor:
            cursor.execute(
                "INSERT INTO ele_foods (poi_id, food_namefirst, food_namefirst_price, food_namefirst_msale, food_namesecond, food_namesecond_price, food_namesecond_msale, food_namethird, food_namethird_price, food_namethird_msale, food_namefour, food_namefour_price, food_namefour_msale, food_namefive, food_namefive_price, food_namefive_msale, food_namesix, food_namesix_price, food_namesix_msale, food_nameseven, food_nameseven_price, food_nameseven_msale, food_nameeight, food_nameeight_price, food_nameeight_msale, food_namenine, food_namenine_price, food_namenine_msale, food_nameten,food_nameten_price, food_nameten_msale) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (item["poi_id"], item["food_namefirst"],item["food_namefirst_price"], item["food_namefirst_msale"], item["food_namesecond"], item["food_namesecond_price"], item["food_namesecond_msale"],
                 item["food_namethird"], item["food_namethird_price"], item["food_namethird_msale"], item["food_namefour"], item["food_namefour_price"], item["food_namefour_msale"],
                 item["food_namefive"], item["food_namefive_price"], item["food_namefive_msale"], item["food_namesix"], item["food_namesix_price"], item["food_namesix_msale"], item["food_nameseven"],
                 item["food_nameseven_price"], item["food_nameseven_msale"], item["food_nameeight"], item["food_nameeight_price"], item["food_nameeight_msale"],
                 item["food_namenine"], item["food_namenine_price"], item["food_namenine_msale"],
                 item["food_nameten"], item["food_nameten_price"], item["food_nameten_msale"]))


    def close_spider(self,spider):
        self.pool.close()





