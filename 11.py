import re
def match(txt):
        patterns = '\w+\S*$'
        if re.search(patterns,  txt):
                return ('Match!')
        else:
                return('Not matched!')
print(match("The quick brown fox jumps over the lazy dog."))
print(match("fgfvgbh hhkl;ok  "))
print(match(" fvbhj bhhh. "))