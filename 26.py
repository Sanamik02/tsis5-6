import re
words = ["PoP Pr", "pddfghj", "prrttp"]

for w in words:
   d= re.match("(P\w+)\W(P\w+)", w)
        
   if d:
      print(d.groups())