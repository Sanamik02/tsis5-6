import re
def match(txt):
        patterns = 'ab{3}$'
        if re.search(patterns,  txt):
                return 'Found a match!'
        else:
                return('Not matched!')

print(match("abbb"))
print(match("aabbbbbc"))