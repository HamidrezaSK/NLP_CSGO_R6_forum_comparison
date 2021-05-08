import json

cleaned_csgo_file = open("../../data/cleaned_csgo.json",'r')
cleaned_r6_file = open("../../data/cleaned_r6.json",'r')


data_cleaned_csgo_file = json.load(cleaned_csgo_file)
data_cleaned_r6_file = json.load(cleaned_r6_file)



words_csgo_file = open("../../data/words_csgo.json",'r')
words_r6_file = open("../../data/words_r6.json",'r')


data_words_csgo_file = json.load(words_csgo_file)
data_words_r6_file = json.load(words_r6_file)


sentence_csgo_file = open("../../data/sentences_csgo.json",'r')
sentence_r6_file = open("../../data/sentences_r6.json",'r')


data_sentence_csgo_file = json.load(sentence_csgo_file)
data_sentence_r6_file = json.load(sentence_r6_file)


unique_csgo_words = set(data_words_csgo_file)
unique_r6_words = set(data_words_r6_file)

common_words= unique_csgo_words & unique_r6_words
uncommon_words=unique_csgo_words ^ unique_r6_words
all_words = unique_csgo_words | unique_r6_words

print("All csgo doc count:",len(data_cleaned_csgo_file))
print("All r6 doc count:",len(data_cleaned_r6_file))

print("All csgo words count:",len(data_words_csgo_file))
print("All r6 words count:",len(data_words_r6_file))

print("All csgo sentence count:",len(data_sentence_csgo_file))
print("All r6 sentence count:",len(data_sentence_r6_file))

print("All unique csgo words count:",len(unique_csgo_words))
print("All unique r6 words count:",len(unique_r6_words))

print("Common words count:",len(common_words))
print("Uncommon words count:",len(uncommon_words))



count_csgo_words = {}
count_r6_words = {}

for word in data_words_csgo_file:
    if(word in count_csgo_words):
        count_csgo_words[word]+=1
    else:
        count_csgo_words[word]=1


for word in data_words_r6_file:
    if(word in count_r6_words):
        count_r6_words[word]+=1
    else:
        count_r6_words[word]=1

count_csgo_words={k: v for k, v in sorted(count_csgo_words.items(), key=lambda item: item[1],reverse=True)}
count_r6_words={k: v for k, v in sorted(count_r6_words.items(), key=lambda item: item[1],reverse=True)}



top_csgo_uncommon_words = {}
top_r6_uncommon_words = {}

for k,v in count_csgo_words.items():
    if k in uncommon_words:
        top_csgo_uncommon_words[k] = v
    if(len(top_csgo_uncommon_words)>=10):
        break

for k,v in count_r6_words.items():
    if k in uncommon_words:
        top_r6_uncommon_words[k] = v
    if(len(top_r6_uncommon_words)>=10):
        break

print("Top sorted uncommon csgo words count:",top_csgo_uncommon_words)
print("Top sorted uncommon r6 words count:",top_r6_uncommon_words)

#calculate RelativeNormalizedFrequency

csgo_relative_normalized_frequency = {}
r6_relative_normalized_frequency = {}

for word in common_words:
    csgo_relative_normalized_frequency[word]=(count_csgo_words[word]/len(data_words_csgo_file))/(count_r6_words[word]/len(data_words_r6_file))
    r6_relative_normalized_frequency[word]=(count_r6_words[word]/len(data_words_r6_file))/(count_csgo_words[word]/len(data_words_csgo_file))


csgo_relative_normalized_frequency={k: v for k, v in sorted(csgo_relative_normalized_frequency.items(), key=lambda item: item[1],reverse=True)}
r6_relative_normalized_frequency={k: v for k, v in sorted(r6_relative_normalized_frequency.items(), key=lambda item: item[1],reverse=True)}

top_csgo_relative_normalized_frequency_words={}
top_r6_relative_normalized_frequency_words={}

for k,v in csgo_relative_normalized_frequency.items():
    top_csgo_relative_normalized_frequency_words[k] = v
    if(len(top_csgo_relative_normalized_frequency_words)>=10):
        break

for k,v in r6_relative_normalized_frequency.items():
    top_r6_relative_normalized_frequency_words[k] = v
    if(len(top_r6_relative_normalized_frequency_words)>=10):
        break


print("Top relative_normalized_frequency csgo words:",top_csgo_relative_normalized_frequency_words)
print("Top relative_normalized_frequency r6 words :",top_r6_relative_normalized_frequency_words)


