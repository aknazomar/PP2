#1
x = 5
print(x > 0 and x < 10) #prints true
print(x > 0 and x > 10) #print false

#2
y = 12
print(y < 10 or y == 12) #true 
print(y < 10 or y > 20) #false

#3
is_raining = True
print(not is_raining) # flips true to false 

#4
age = 20
has_ticket = True
print(age >= 18 and has_ticket)  # True (adult AND has ticket)
print(age < 18 or has_ticket)    # True (has ticket, even if not under 18)

#5
temperature = 25
is_hot = temperature > 30
is_cold = temperature < 10
print(not is_hot and not is_cold)  # True (comfortable weather)