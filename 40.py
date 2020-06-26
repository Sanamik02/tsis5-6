import re

txt="London is the capital of Great Britain"
d= re.sub("[ ]", "", txt)
print(d)