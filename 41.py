import re
d = "!@# asdfg1 - 23455\||6" 
pattern= re.compile("[\W]")
x=pattern.sub("", d)
print(x)