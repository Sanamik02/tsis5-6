import re
text = "asdfgh cvbn fghjy cnbgj d"

shortword = re.compile(r'\W*\b\w{1,3}\b')
d=shortword.sub('', text)
print(d)