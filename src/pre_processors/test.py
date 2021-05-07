import emoji
import re
# print(" \u00a1\u00a1\ud83d")
a = "Originally posted by \u00a1\u00a1\ud83d\udc9bLEON TRADE"
if(r"\u" in a):

    print("d")
b = a.encode('utf-16', 'surrogatepass').decode('utf-16')
c = a.split()
c = [idx for idx in c if not re.findall("[^\u0000-\u05C0\u2100-\u214F]+", idx)]
# b = a.find('\u')
# while b!= -1:
#     temp = a[b:b+6]
#     a.strip(temp)
# # if('\ud83d' in emoji.UNICODE_EMOJI):
# #     print("fuck")




print (c)