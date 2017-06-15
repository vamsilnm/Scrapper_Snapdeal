# -*- coding: utf-8 -*-
from scrapy.selector import Selector
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.item import Field,Item 
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from snapdeal.SnapdealItem import 

class SnapdealItem(scrapy.Item):
	text = Field()
	



class Snapdeal(CrawlSpider):

	name = "snapdeal_spider"
	allowed_domains = ["snapdeal.com"]
	start_urls = ['https://www.snapdeal.com/product/unique-for-men-navy-formal/623703512756/reviews?page=1&sortBy=HELPFUL#defRevPDP']
	rules = (
	Rule(LinkExtractor(allow=r'reviews\?page=[0-9]{2}&sortBy=HELPFUL#defRevPDP'), callback="parse_start_url", follow= True),
	)
	def parse_start_url(self, response):
		items = []
		reviews = Selector(response).xpath('//div[@id = "content_wrapper"]/div[@class="theme-wrapper container-fluid"]/div[@class= "wrapper"]/div[@class="row"]/div[@class = "product-detail-card-left"]/div[@class="col-xs-19 box-size-property"]/div[@class="comp comp-customer-review"]/div[@class="customer_review"]/div[@class="whitebx"]/div[@id="defaultReviewsCard"]/div[@class="reviewareain clearfix"]')
		
		for review in reviews:
			item = SnapdealItem()
			item['text'] = review.xpath('div[@class="commentreview"]/div[@class="commentlist first jsUserAction"]/div[@class="text"]/div[@class="user-review"]/p/text()').extract()
			# print item['text']

			if len(item['text']) != 0:
				items.append(item)
			yield item
		# return items
		






