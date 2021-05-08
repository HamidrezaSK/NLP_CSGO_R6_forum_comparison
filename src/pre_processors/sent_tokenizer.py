from nltk.tokenize import sent_tokenize
import json
import re

file = open("../../data/cleaned_csgo.json",'r')

data = json.load(file)

sentences = []
for line in data:
    comment = line["csgo"]
    sentences.extend(sent_tokenize(comment))
with open('../../data/sentences_csgo.json', 'w') as outfile:
    json.dump(sentences, outfile)
file.close()


file = open("../../data/cleaned_r6.json",'r')

data = json.load(file)

sentences = []
for line in data:
    comment = line["r6"]
    sentences.extend(sent_tokenize(comment))
with open('../../data/sentences_r6.json', 'w') as outfile:
    json.dump(sentences, outfile)
file.close()