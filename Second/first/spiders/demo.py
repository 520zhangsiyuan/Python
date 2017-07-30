import scrapy
import lxml.html
from selenium import webdriver
from first.items import FirstItem
import time
class Demo_data(scrapy.Spider):
    name = 'demo'
    start_urls = ['http://data.nowgoal.com/OddsCompBasket/284834.html']
    def parse(self,response):
        items = []
        scrapy.selector.Selector(response)
        #打开浏览器
        driver = webdriver.Firefox()
        #打开网址
        driver.get('http://data.nowgoal.com/OddsCompBasket/284834.html')
        #获取加载完的网页数据
        sel = driver.page_source
        #print '*******************************'
        #解析
        doc = lxml.html.fromstring(sel)
        sites =doc.xpath('//table[@id="Table1"]/tbody/tr')
        for site in sites:
            item = FirstItem()
            #print '*******************************'
            #print str(site.xpath('td[1]/font/text()'))
            item['Sbobet'] = str(site.xpath('td[1]/font/text()'))
            item['Easybet'] = str(site.xpath('td[2]/font/text()'))
            item['Crown'] = str(site.xpath('td[3]/font/text()'))
            item['Bet365'] = str(site.xpath('td[4]/font/text()'))
            item['Vcbet'] = str(site.xpath('td[5]/font/text()'))
            item['time'] = str(site.xpath('td[6]/text()'))
            items.append(item)
            
        return items
        driver.quit()

