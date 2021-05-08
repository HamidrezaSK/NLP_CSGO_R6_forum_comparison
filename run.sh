#!/bin/sh
source env/bin/activate
cd src/crawler/
scrapy crawl r6 -O ../../data/r6.json
scrapy crawl csgo -O ../../data/csgo.json
cd ../../src/pre_processors
python clean_data.py 
python sent_tokenizer.py
python word_tokenizer.py
cd ../stats
python exract_stats.py 
