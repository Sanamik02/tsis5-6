import re
ip = "123.05.555.050"
d= re.sub('\.[0]*', '.', ip)
print(d)