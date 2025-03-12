import requests
import scrapy
from pathlib import Path

class MovieSpider(scrapy.Spider):
    name = 'movies'

    def start_requests(self):
        urls = [
            'https://www.cinema21.com',
            'https://www.hollywoodtheatre.org',
            'https://pdx.livingroomtheaters.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self,response):
        page=response.url.split('/')[-2]
        filename = f'homepage-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Save file {filename}')


