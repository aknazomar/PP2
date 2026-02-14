to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

to_word = {v: k for k, v in to_digit.items()}

def decode(s):
    number = ""
    for i in range(0, len(s), 3):
        number += to_digit[s[i:i+3]]
    return int(number)

def encode(num):
    if num == 0:
        return "ZER"
    result = ""
    for d in str(num):
        result += to_word[d]
    return result

expr = input().strip()

for op in "+-*":
    if op in expr:
        left, right = expr.split(op)
        operator = op
        break

a = decode(left)
b = decode(right)

if operator == "+":
    res = a + b
elif operator == "-":
    res = a - b
else:
    res = a * b

print(encode(res))