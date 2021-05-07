from nltk.tokenize import sent_tokenize
import json
import re
import emoji

file = open("cleaned_csgo.json",'r')

data = json.load(file)

sentences = []
for line in data:
    comment = line["csgo"]
    sentences.extend(sent_tokenize(comment))
with open('sentences.json', 'w') as outfile:
    json.dump(sentences, outfile)
file.close()