import re

txt ="asdf asdfg rghgfd rrtg efgh"

d= re.findall("[ae]\w+", txt)

print(d)