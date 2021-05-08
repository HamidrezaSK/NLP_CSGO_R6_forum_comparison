#!/bin/sh
source env/bin/activate
cd src/crawler/
scrapy crawl r6 -O ../../data/r6.json
scrapy crawl csgo -O ../../data/csgo.json
cd ../../
python src/pre_processors/clean_data.py 
python src/pre_processors/sent_tokenizer.py
python src/pre_processors/word_tokenizer.py
python src/stats/exract_stats.py 
