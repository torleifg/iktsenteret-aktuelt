#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import scrapy, json
from bs4 import BeautifulSoup
from aktuelt.items import Document

class DocumentSpider(scrapy.Spider):
    name = "documents"

    def start_requests(self):
        with open('index.json') as json_data:
            urls = json.load(json_data)
            for url in urls:
                request = scrapy.Request(url=url['href'], callback=self.parse)
                request.meta['date'] = url['date']
                request.meta['title'] = url['title']
                yield request
    
    def parse(self, response):
        item = Document()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        item['date'] = response.meta['date']
        item['title'] = response.meta['title']
        
        if soup.find(id="blog2016-panel"):
            ingress = soup.find("div", class_="pane-node-field-ingress")
            body = soup.find("div", class_="pane-node-body")

            if ingress is None:
                item['content'] = body.get_text(" ", strip=True)
            elif body is None:
                item['content'] = ingress.get_text(" ", strip=True)
            else:
                item['content'] = ' '.join([ingress.get_text(" ", strip=True), body.get_text(" ", strip=True)])
                
        elif soup.find(id="article-panel-2016"):
            ingress = soup.find("div", class_="pane-node-field-intro-text")
            body = soup.find("div", class_="pane-node-field-text")
            
            if ingress is None:
                item['content'] = body.get_text(" ", strip=True)
            elif body is None:
                item['content'] = ingress.get_text(" ", strip=True)
            else:
                item['content'] = ' '.join([ingress.get_text(" ", strip=True), body.get_text(" ", strip=True)])

        return item