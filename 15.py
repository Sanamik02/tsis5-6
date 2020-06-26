import re
def ans(string):
    txt = re.compile(r"^5")
    if txt.match(string):
        return True
    else:
        return False
print(ans("555555"))
print(ans("12345"))