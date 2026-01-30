a = "Hello"
print(a)

#multiline string
b = '''Hello,
World!'''
print(b)

#string indexing
a = "Hello, World!"
print(a[1])

#looping
for x in "banana":
    print(x)

#string length
a = "Hello, World!"
print(len(a))

#check string
a = "men oskende sayahatshy dara bolamyn"
print("sayahatshy" in a)

#check string not in
a = "men oskende sayahatshy dara bolamyn"
print("Saya" not in a)

#slicing strings
b = "Hello, World!"
print(b[2:5])
print(b[:5])
print(b[2:])
print(b[-5:-2])

#modify string
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

#string concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#F-strings
name = "John"
age = 36
txt = f"My name is {name}, and I am {age}"
print(txt)

#wscape characters
txt = "We are the so-called \"Vikings\" from the north."
print(txt)