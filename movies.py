import scrapy
from pathlib import Path
from html.parser import HTMLParser
import sys
import sqlite3

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

def main():
    #upon program call, spider should scrape and overwrite sqlite database
    #then print sqlite results, formatted, to terminal
    #need to set up sqlite3 in another file? pipelines?