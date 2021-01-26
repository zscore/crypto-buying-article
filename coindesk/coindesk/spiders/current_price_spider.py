import datetime
import scrapy
import time


class CoinDeskCurrentSpider(scrapy.Spider):
    name = "coindesk_current"

    def start_requests(self):
        for i in range(1, 43):
            url = f"https://coinmarketcap.com/{i}/"
            time.sleep(5)
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):
        page = response.url.split("/")[-2]
        today_date_str = datetime.date.today().strftime("%Y%m%d")
        filename = f'coinmarketcap-current-{page}-{today_date_str}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')