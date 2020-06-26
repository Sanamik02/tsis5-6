import re
txt="AbcdEfghIgklmNopqrStuxyz"
d=re.findall("[A-Z][^A-Z]*", txt)
print(d)