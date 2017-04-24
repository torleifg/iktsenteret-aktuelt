#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import json

from nltk.tokenize import word_tokenize, sent_tokenize

class NewsCorpus:    
    def __init__(self, filename):
        self.filename = filename
        self.words, self.sents = [], []
        with open(self.filename) as json_data:
            self.documents = json.load(json_data)
    
    def tokenize_words(self): 
        for document in self.documents:
            #self.words += word_tokenize(document['content'], language='norwegian') #nltk3
            self.words += word_tokenize(document['content'].encode('utf-8')) #nltk2
                           
    def tokenize_sents(self):
        for document in self.documents:
            #self.sents += sent_tokenize(document['content'], language='norwegian') #nltk3
            self.sents += sent_tokenize(document['content'].encode('utf-8')) #nltk2