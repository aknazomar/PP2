#1 example
x = 5
y = 10

print(x < y)   # True
print(x > y)   # False

#2 example
age = 18

if age >= 18:
    print("you can vote")
else:
    print("you can't vote")

#3 example
is_student = True
has_ticket = False

if is_student and has_ticket:
    print("Welcome!")
else:
    print("You can buy a ticket there!")

#4 example
temperature = int(input("Please, enter the current temperature: "))
is_hot = temperature > 30
is_cold = temperature < 10
if is_hot:
    print("Hot!")
elif is_cold:
    print("Cold!")
else:
    print("Yaaay!")

#5 example
discount = input("Please enter yes, if it has discount, else enter no: ")
if discount.lower() == "yes":
    dicsount = True
else:
    discount = False

if discount:
    print("Yaaay!")
else:
    print("mmm...")

#