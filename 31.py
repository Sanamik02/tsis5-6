import re

d="I hope that I will be better"
x= re.sub("[  ,.]", ":", d )
print(x)