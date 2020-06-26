import re
def date(dt):
    return re.sub(r"(\d{4})-(\d{1,2})-(\d{1,2})","\\3-\\2-\\1",dt)

x="2020-26-06"
print(x)
print(date(x))