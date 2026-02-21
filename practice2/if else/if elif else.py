# Example 1
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
else:
    print("C or lower")
print(" ") #B

# Example 2
temperature = 15
if temperature < 10:
    print("Cold")
elif temperature < 25:
    print("Warm")
else:
    print("Hot")
print(" ") #Warm!

# Example 3
day = "Saturday"
if day == "Monday":
    print("Start of the week")
elif day == "Friday":
    print("Almost weekend")
elif day == "Saturday" or day == "Sunday":
    print("Weekend!")
else:
    print("Midweek")
print(" ") #Weekend!

# Example 4
speed = 120
if speed < 60:
    print("Slow")
elif speed <= 100:
    print("Normal")
else:
    print("Too fast!")
print(" ") # Too fast!

# Example 5
color = "green"
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait")
elif color == "green":
    print("Go")
else:
    print("Unknown signal") #Go!