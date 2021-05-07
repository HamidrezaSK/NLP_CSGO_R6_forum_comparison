import pycld2 as cld2
import json
import re
import emoji
file = open("../crawler/csgo.json",'r')

  
# returns JSON object as 
# a dictionary
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
            if(english_part != english_part.encode('utf-16', 'surrogatepass').decode('utf-16')):
                print("found one")
            parts=english_part.split()
            parts = [idx for idx in parts if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)]
            # for i in range(len(parts)-1,-1,-1):
            #     if(parts[i] != parts[i].encode('utf-16', 'surrogatepass').decode('utf-16')):
            #         print(parts.pop(i))
            english_part = " ".join(parts)
            # english_part=re.sub("(\uXXXX)", "'", english_part)
            cleaned_data.append({
            'csgo': english_part
            })

    
  
with open('cleaned_csgo.json', 'w') as outfile:
    json.dump(cleaned_data, outfile)
file.close()


# print(text_content[detected_language[1][0]:detected_language[1][0]+detected_language[1][1]])
