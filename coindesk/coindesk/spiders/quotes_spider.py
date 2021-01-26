import datetime
import os
import scrapy
import time


class CoinDeskSpider(scrapy.Spider):
    name = "coindesk"

    def start_requests(self):
        spider_date = datetime.date(2013, 4, 28)
        spider_interval = datetime.timedelta(days=1)
        while spider_date <= (datetime.date.today() - spider_interval):
            str_spider_date = spider_date.strftime("%Y%m%d")
            url = f"https://coinmarketcap.com/historical/{str_spider_date}"
            if not os.path.isfile(f'coinmarketcap-historical-{str_spider_date}.html'):
                yield scrapy.Request(url=url, callback=self.parse)
                time.sleep(5)
            spider_date += spider_interval

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'coinmarketcap-historical-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')