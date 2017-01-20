#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import scrapy
from bs4 import BeautifulSoup

class IndexSpider(scrapy.Spider):
    name = "index"
    start_urls = [
    	'http://iktsenteret.no/aktuelt',
    ]
    
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        documents = soup.find_all("div", class_="views-row")
        
        for document in documents:
            yield {
                   'date': document.find("div", class_="views-field-created").span.string,
                   'title': document.a.string,
                   'href': response.urljoin(document.a.get('href')),
            }
        
        next_page = soup.find("li", class_="pager-next").a.get('href')
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
