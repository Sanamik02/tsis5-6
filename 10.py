import re
def match(txt):
        patterns = '^\w+'
        if re.search(patterns,  txt):
                return ('Match!')
        else:
                return('Not matched!')

print(match("fgfvgbh hhkl;ok  "))
print(match(" fvbhj bhhh. "))