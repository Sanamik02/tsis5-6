import re

txt = "asdf cbhbfk cbhdghjk 25 cgfhfk cbhiuk hvghvb n"

for d in re.finditer("\d+", txt):
    print(d.group(0))
    print(d.start())