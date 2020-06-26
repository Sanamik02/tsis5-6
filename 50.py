import re
txts=["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for txt in txts:
    d=re.sub(r" ?\([^]+\)", "", txt)
    print(d)