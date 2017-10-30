# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from lazada.items import LazadaItem

class LzdSpider(scrapy.Spider):
    name = 'lzd'
    allowed_domains = ['lazada.sg']
    start_urls = ['http://lazada.sg/']

    def parse(self, response):
        print(response.xpath("//title/text()").extract())
        key = "music"
        for i in range(0,1):
            url = "http://www.lazada.sg/catalog/?page="+str(i+1)+"&q="+str(key)
            print(url)
            yield Request(url = url, callback=self.page)

    def page(self,response):
        body = response.body.decode("utf-8", "ignore")
         #productPath[] =  response.xpath("//div[@class='c-product-card__description']/a/@href").extract()
        # for j in range(0,37):
        #     path = response.xpath("//div[@class='c-product-card__description']/a/@href")[j].extract()
        #     url1 = "http://www.lazada.sg"+path
        #     #print(url1)
        #     yield Request(url=url1,callback=self.next)

        for path in response.xpath("//div[@class='c-product-card__description']/a/@href").extract():
            url1 = "http://www.lazada.sg"+path
            #print(url1)
            yield Request(url=url1,callback=self.next)



    def next(self, response):
        item = LazadaItem()
        item['title'] = response.xpath("//h1[@id]/text()").extract()
        item['link'] = (response.url).strip() #Trim space between front and end of the string
        item['brand'] = response.xpath("//div[@class='prod_header_brand_action']/a/span/text()").extract()
        item['price'] =  response.xpath("//div[@class='prod_pricebox_price_final']/span[@id='product_price']/text()").extract()

        comment = response.xpath("//div[@id='review']/a/text()").extract()
        if len(comment) == 0:
            item['comment'] =  "0"
        else:
            item['comment'] = comment

        yield item
