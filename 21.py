import re
result = re.search(r'exercises','Python exercises, PHP exercises, C# exercises')
d=result.group(0)
print(d)