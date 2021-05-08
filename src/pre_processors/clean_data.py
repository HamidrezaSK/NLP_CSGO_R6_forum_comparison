import pycld2 as cld2
import json
import re
file = open("../../data/csgo.json",'r')

data = json.load(file)

cleaned_data = []
for line in data:
    comment = line["csgo"]
    _, _, _, detected_language = cld2.detect(comment,  returnVectors=True)
    for obj in detected_language:
        if(obj[2] == "ENGLISH"):
            start = obj[0]
            end = obj[0]+obj[1]
            english_part = comment[start:end]
            english_part = english_part.strip()
            parts=english_part.split()
            parts = [idx for idx in parts if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)]
            english_part = " ".join(parts)
            cleaned_data.append({
            'csgo': english_part
            })

    
  
with open('../../data/cleaned_csgo.json', 'w') as outfile:
    json.dump(cleaned_data, outfile)
file.close()


file = open("../../data/r6.json",'r')

  

data = json.load(file)

cleaned_data = []
for line in data:
    comment = line["r6"]
    _, _, _, detected_language = cld2.detect(comment,  returnVectors=True)
    for obj in detected_language:
        if(obj[2] == "ENGLISH"):
            start = obj[0]
            end = obj[0]+obj[1]
            english_part = comment[start:end]
            english_part = english_part.strip()
            parts=english_part.split()
            parts = [idx for idx in parts if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)]
            english_part = " ".join(parts)
            cleaned_data.append({
            'r6': english_part
            })

    
  
with open('../../data/cleaned_r6.json', 'w') as outfile:
    json.dump(cleaned_data, outfile)
file.close()
