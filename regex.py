import re
pattern = "apple"
if re.match(pattern, "apple"):
    print('True')
else:
    print('False')
# findall
print(re.findall(pattern, 'xyz'))

# search
if re.search(pattern, "applesunil", flags=0):
    print('Found')
    
# sub(pattern, repl, string, count, flags)
string = 'Its a dog'
pattern = 'dog'
print(re.sub(pattern, 'cat', string, count=0, flags=0))

# CHARACTER AND CHARACTER SEQUENCES
# ^ - Matches the beginning of a line
# $ - Matches the end of a line
# . - Matches any character
# \d - Matches any digit
# \D - Matches any non digit
# \s - Matches whitespace
# \S - Matches any non-whitespace.