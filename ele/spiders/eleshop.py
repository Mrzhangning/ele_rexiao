# -*- coding: utf-8 -*-
import scrapy

from scrapy_splash import SplashRequest
from ele.items import EleShopItem
from ele.shoplist import get_shopid_list
import json


class EleshopSpider(scrapy.Spider):
    name = "eleshop"
    allowed_domains = ["www.ele.me/shop"]

    #website_possible_httpstatus_list = [403]
    #handle_httpstatus_list = [403]

    def start_requests(self):
        shop_list = get_shopid_list()
        start_url = "https://www.ele.me/restapi/shopping/v2/menu?restaurant_id="
        urls = ['{}{}'.format(start_url, i) for i in shop_list]

        for url in urls:
            # http://112.86.73.52:53281
            # yield SplashRequest(url=url, callback=self.parse,args={"wait":0.5},headers = {'Content-Type': 'application/json'})
            yield scrapy.Request(url=url, callback=self.parse,)

    def parse(self, response):
        if response.body == "banned":
            req = response.request
            req.meta["change_proxy"] = True
            yield req
        else:
            data = response.text
            jdata = json.loads(data)
            items = EleShopItem()
            caipin = jdata[0]

            if caipin['name'] == '热销':
                rexiao = caipin['foods']
                items["poi_id"]= rexiao[0]['restaurant_id']
                try:
                    items['food_namefirst'] = rexiao[0]['specfoods'][0]['name']
                    items['food_namefirst_price'] = rexiao[0]['specfoods'][0]['price']
                    items['food_namefirst_msale'] = rexiao[0]['month_sales']
                except:
                    items['food_namefirst'] = '空'
                    items['food_namefirst_price'] = '0'
                    items['food_namefirst_msale'] = '0'
                try:
                    items['food_namesecond'] = rexiao[1]['specfoods'][0]['name']
                    items['food_namesecond_price'] = rexiao[1]['specfoods'][0]['price']
                    items['food_namesecond_msale'] = rexiao[1]['month_sales']
                except:
                    items['food_namesecond'] = '空'
                    items['food_namesecond_price'] = '0'
                    items['food_namesecond_msale'] = '0'
                try:
                    items['food_namethird'] = rexiao[2]['specfoods'][0]['name']
                    items['food_namethird_price'] = rexiao[2]['specfoods'][0]['price']
                    items['food_namethird_msale'] = rexiao[2]['month_sales']
                except:
                    items['food_namethird'] = '空'
                    items['food_namethird_price'] = '0'
                    items['food_namethird_msale'] = '0'
                try:
                    items['food_namefour'] = rexiao[3]['specfoods'][0]['name']
                    items['food_namefour_price'] = rexiao[3]['specfoods'][0]['price']
                    items['food_namefour_msale'] = rexiao[3]['month_sales']
                except:
                    items['food_namefour'] = '空'
                    items['food_namefour_price'] = '0'
                    items['food_namefour_msale'] = '0'
                try:
                    items['food_namefive'] = rexiao[4]['specfoods'][0]['name']
                    items['food_namefive_price'] = rexiao[4]['specfoods'][0]['price']
                    items['food_namefive_msale'] = rexiao[4]['month_sales']
                except:
                    items['food_namefive'] = '空'
                    items['food_namefive_price'] = '0'
                    items['food_namefive_msale'] = '0'
                try:
                    items['food_namesix'] = rexiao[5]['specfoods'][0]['name']
                    items['food_namesix_price'] = rexiao[5]['specfoods'][0]['price']
                    items['food_namesix_msale'] = rexiao[5]['month_sales']
                except :
                    items['food_namesix'] = "空"
                    items['food_namesix_price'] = "0"
                    items['food_namesix_msale'] = "0"
                try:
                    items['food_nameseven'] = rexiao[6]['specfoods'][0]['name']
                    items['food_nameseven_price'] = rexiao[6]['specfoods'][0]['price']
                    items['food_nameseven_msale'] = rexiao[6]['month_sales']
                except:
                    items['food_nameseven'] = "空"
                    items['food_nameseven_price'] = "0"
                    items['food_nameseven_msale'] = "0"
                try:
                    items['food_nameeight'] = rexiao[7]['specfoods'][0]['name']
                    items['food_nameeight_price'] = rexiao[7]['specfoods'][0]['price']
                    items['food_nameeight_msale'] = rexiao[7]['month_sales']
                except:
                    items['food_nameeight'] = "空"
                    items['food_nameeight_price'] = "0"
                    items['food_nameeight_msale'] = "0"
                try:
                    items['food_namenine'] = rexiao[8]['specfoods'][0]['name']
                    items['food_namenine_price'] = rexiao[8]['specfoods'][0]['price']
                    items['food_namenine_msale'] = rexiao[8]['month_sales']
                except:
                    items['food_namenine'] = "空"
                    items['food_namenine_price'] = "0"
                    items['food_namenine_msale'] = "0"
                try:
                    items['food_nameten'] = rexiao[9]['specfoods'][0]['name']
                    items['food_nameten_price'] = rexiao[9]['specfoods'][0]['price']
                    items['food_nameten_msale'] = rexiao[9]['month_sales']
                except:
                    items['food_nameten'] = "空"
                    items['food_nameten_price'] = "0"
                    items['food_nameten_msale'] = "0"
                yield items



