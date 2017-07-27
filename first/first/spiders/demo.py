import scrapy
from first.items import FirstItem
class Demo_data(scrapy.Spider):
    name = 'demo'
    #链接需要爬取的网站
    allowed_domains = ['nowgoal.com']
    start_urls = ['http://data.nowgoal.com/OddsCompBasket/284834.html']
    def parse(self,response):
        #爬取数据
        items = []
        sel =scrapy.selector.Selector(response)
        sites = sel.xpath('//body/div[@id="main"]/table/tr/td/table[@id="Table1"]/tr')
        for site in sites:
            item = FirstItem()
            item['Sbobet'] = site.xpath('td[1]/font/text()').extract()
            item['Easybet'] = site.xpath('td[2]/font/text()').extract()
            item['Crown'] = site.xpath('td[3]/font/text()').extract()
            item['Bet365'] = site.xpath('td[4]/font/text()').extract()
            item['Vcbet'] = site.xpath('td[5]/font/text()').extract()
            item['time'] = site.xpath('td[6]/text()').extract()
            items.append(item)
        return items
