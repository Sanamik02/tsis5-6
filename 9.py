import re
def match(txt):
        patterns = 'a.*?b$'
        if re.search(patterns,  txt):
                return 'Match!'
        else:
                return('Not matched!')

print(match("ab"))
print(match("abcd"))
print(match("cghjjb"))