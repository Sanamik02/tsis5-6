import re
def match(txt):
        patterns = 'ab*?'
        if re.search(patterns,  txt):
                return ('Match!')
        else:
                return('Not matched!')

print(match("acbb"))
print(match("abcde"))
print(match("abbc"))