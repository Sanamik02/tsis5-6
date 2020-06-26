import re
def num(string):
    txt = re.compile(r".*[0-9]$")
    if txt.match(string):
        return True
    else:
        return False

print(num('zxcvbhjkjl12345'))
print(num('fcgvhbjknlm5'))
