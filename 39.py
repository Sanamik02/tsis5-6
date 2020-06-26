import re

txt="I gonna to    present     my     work"
d=re.sub(" +"," ",txt)
print(d)