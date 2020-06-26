import re

d="I hope that I will be better"
x= re.sub("[  ,.]", ":", d , 2)
print(x)