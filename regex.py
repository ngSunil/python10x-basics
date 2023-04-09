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
# * - Repeats a character zero or more times
# + - Repeats a character one or more times
# ( - Indicates where a string extractions is to start
# ) - Indicates where the string extraction is to end
# ? - Matches the expression 0 to 1 lines

string = 'This is the test screen 56'
# pattern = '^T'
# pattern = 'n$'
# pattern = '.'
# pattern = '^T.'
# pattern = '\d'
# pattern = '\D'
# pattern = '\s'
# pattern = 'he*'
pattern = 'he+'

print(re.findall(pattern, string))

string = 'from sun.aec@gmail.com'
pattern = '^from.(\S+@\S+)'
print(re.findall(pattern, string))
# []
# [aeiou] - Matches a single character in the listed set
# [^xyz] - Matches a single character
# [a-z 0-9] - Set of characters can include range
# {}
string = 'pythonW'
# pattern = "[aeiou]"
# pattern = "[^aeiou]"
pattern = "[a-z 0-9]"
print(re.findall(pattern, string))