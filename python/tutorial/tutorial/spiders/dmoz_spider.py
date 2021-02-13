import scrapy
from scrapy import item

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz-odp.org']
    start_urls = [
        'https://dmoz-odp.org/Computers/Programming/Languages/Python/Books/',
        'https://dmoz-odp.org/Computers/Programming/Languages/Python/Resources/'
    ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="title-and-desc"]')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/div/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('div/text()').extract()
            items.append(item)

        return items
            