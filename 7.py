import re
def match(txt):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  txt):
                return ('Found a match!')
        else:
                return('Not matched!')

print(match("abc_xcv"))
print(match("aab_Abbbc"))
print(match("aab_abbbc"))