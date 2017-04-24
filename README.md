### Crawler

$ conda create --name environment scrapy beautifulsoup4 nltk=2

$ git clone https://github.com/torleifg/iktsenteret-aktuelt.git

$ source activate environment

$ cd iktsenteret-aktuelt/crawler/aktuelt/

$ scrapy crawl index -o index.json

$ scrapy crawl documents -o documents.json

### NLP

$ cd iktsenteret-aktuelt/nlp/

$ python

````
>>> import nlp, nltk
>>> corpus = nlp.NewsCorpus('../crawler/aktuelt/documents.json')
>>> corpus.tokenize_words()
>>> text = nltk.Text(corpus.words)
>>> text.generate()
````

Natural Language Processing with Python
http://www.nltk.org/book_1ed/



