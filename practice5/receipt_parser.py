# 1 (Write a Python program that matches 
# a string that has an 'a' followed by 
# zero or more 'b''s.)

import re

text = "abbb"
pattern = r"ab*"

if re.fullmatch(pattern, text):
    print("Match found")
else:
    print("No match")


# 2 (Write a Python program that matches 
# a string that has an 'a' followed by 
# two to three 'b'.)

import re

text = "abbb"
pattern = r"ab{2,3}"

if re.fullmatch(pattern, text):
    print("Match found")

# 3 (Write a Python program to find sequences 
# of lowercase letters joined with a underscore.)

import re

text = "hello_world test_data example"
pattern = r"[a-z]+_[a-z]+"

result = re.findall(pattern, text)
print(result)


# 4 (Write a Python program to find the sequences
# of one upper case letter followed by lower case 
# letters.)

import re

text = "Hello World Python Programming"
pattern = r"[A-Z][a-z]+"

print(re.findall(pattern, text))

# 5 (Write a Python program that matches a string 
# that has an 'a' followed by anything, ending in 'b'.)

import re

text = "axxxb"
pattern = r"a.*b"

if re.fullmatch(pattern, text):
    print("Match")

# 6 (Write a Python program to replace all occurrences 
# of space, comma, or dot with a colon.)

import re

text = "Hello, world. Python is fun"
result = re.sub(r"[ ,.]", ":", text)

print(result)

# 7 (Write a python program to convert 
# snake case string to camel case string.)

import re

text = "snake_case_example"

result = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), text)

print(result)

# 8 (Write a Python program to split a string 
# at uppercase letters.)

import re

text = "SplitThisString"

result = re.split(r"(?=[A-Z])", text)

print(result)

# 9 (Write a Python program to insert spaces between words 
# starting with capital letters.)

import re

text = "HelloWorldPython"

result = re.sub(r"([A-Z])", r" \1", text).strip()

print(result)

# 10 (Write a Python program to convert a given 
# camel case string to snake case.)
import re

text = "camelCaseString"

result = re.sub(r"([A-Z])", r"_\1", text).lower()

print(result)