# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyIPItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    type = scrapy.Field()



class EleShopItem(scrapy.Item):

    # 商家ID
    poi_id = scrapy.Field()
    # 热销菜品1
    food_namefirst = scrapy.Field()
    food_namefirst_price=scrapy.Field()
    food_namefirst_msale=scrapy.Field()
    # 热销菜品2
    food_namesecond = scrapy.Field()
    food_namesecond_price = scrapy.Field()
    food_namesecond_msale = scrapy.Field()
    # 热销菜品3
    food_namethird = scrapy.Field()
    food_namethird_price = scrapy.Field()
    food_namethird_msale = scrapy.Field()
    # 热销菜品4
    food_namefour = scrapy.Field()
    food_namefour_price = scrapy.Field()
    food_namefour_msale = scrapy.Field()
    # 热销菜品5
    food_namefive = scrapy.Field()
    food_namefive_price = scrapy.Field()
    food_namefive_msale = scrapy.Field()
    # 热销菜品6
    food_namesix = scrapy.Field()
    food_namesix_price = scrapy.Field()
    food_namesix_msale = scrapy.Field()
    # 热销菜品7
    food_nameseven = scrapy.Field()
    food_nameseven_price = scrapy.Field()
    food_nameseven_msale = scrapy.Field()
    # 热销菜品8
    food_nameeight = scrapy.Field()
    food_nameeight_price = scrapy.Field()
    food_nameeight_msale = scrapy.Field()
    # 热销菜品9
    food_namenine = scrapy.Field()
    food_namenine_price = scrapy.Field()
    food_namenine_msale = scrapy.Field()
    # 热销菜品10
    food_nameten = scrapy.Field()
    food_nameten_price = scrapy.Field()
    food_nameten_msale = scrapy.Field()


