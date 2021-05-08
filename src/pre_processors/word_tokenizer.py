import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import json
import re


file = open("../../data/cleaned_csgo.json",'r')

data = json.load(file)

words = []
for line in data:
    comment = line["csgo"]
    words.extend(word_tokenize(comment))
with open('../../data/words_csgo.json', 'w') as outfile:
    json.dump(words, outfile)
file.close()

file = open("../../data/cleaned_r6.json",'r')

data = json.load(file)

words = []
for line in data:
    comment = line["r6"]
    words.extend(word_tokenize(comment))
with open('../../data/words_r6.json', 'w') as outfile:
    json.dump(words, outfile)
file.close()