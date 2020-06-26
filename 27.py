import re
text = "A-123, B-234, C-345"
d = re.split("\D+", text)

for x in d:
    print(x)