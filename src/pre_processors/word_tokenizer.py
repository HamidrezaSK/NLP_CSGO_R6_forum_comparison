import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import json
import re
import emoji

file = open("cleaned_csgo.json",'r')

data = json.load(file)

words = []
for line in data:
    comment = line["csgo"]
    words.extend(word_tokenize(comment))
with open('words.json', 'w') as outfile:
    json.dump(words, outfile)
file.close()