
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
# Lesson 08: Loops
from turtle import title

print("")
title = " Lesson 08: Loops ".upper()
# Lesson 08: Loops
print(title.center(50, "="))

# How does this loop work while, then break?
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

# %%    
# How does this loop work while, after continue?
value = 1
while value <= 10:
  value += 1
  if value == 5:
    continue
  print(value)
else:
  print("Value is now equal to " + str(value))

# %%
print("")
title = " How does this loop work with string array ".upper()
print(title.center(50, "="))
# How does this loop work with string array?
names = ["John", "Paul", "George", "Ringo"]
for x in names:
    print(x)

for x in "Mississippi":
    print(x)

for x in names:
    if x == "George":
        continue
    print(x)

for x in range(4):
    print(x) # Output: 0, 1, 2, 3

for x in range(2, 4):
  print(x) # Output: 2, 3

for x in range(5, 101, 5):
  print(x) # Output: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100
else:
  print("Glad that\'s over!")
# %%
print("")
title = " How does this loop work with nested loops ".upper()
print(title.center(50, "="))
# How does this loop work with nested loops, please explain me two nested loops with the following code structure?
names = ["Sisovin", "Sovanny", "Viphop"]
actions = ["codes", "eats", "sleeps"]
for name in names:
    for action in actions:
        print(name +" "+ action +".")
print("")
for action in actions:
    for name in names:
        print(name +" "+ action +".")
print("")
# Display a list of names and actions each person is doing at least three rows with two columns.
# Iterate through each name and action
for i, name in enumerate(names, start=1):
    print(f"{i}. {name} {actions[1]}.")

print("")
# Assuming names and actions are predefined lists
# names = ["Alice", "Bob", "Charlie"]
# actions = ["running", "jumping", "swimming"]

# Outer loop iterates over names
for i, name in enumerate(names, start=1):
    print(f"{i}. {name} is:")
    # Inner loop iterates over actions
    for action in actions:
        print(f"   - {action}")

print("")      
# names = ["Sisovin", "Sovanny", "Viphop"]
# actions = ["codes", "eats", "sleeps"]

for i, name in enumerate(names, start=1):
    for action in actions:
        # Check if the current name is Sovanny and the action is eats
        if name == "Sovanny" and action == "eats":
            continue  # Skip this iteration
        print(f"{i}. {name} {action}.")
          
# %%
