# HarshaMalipeddi
# a list of menu items
food = ["Burger", "Shake", "Fries"]

print(food[0], "is located at index 0.")
print(food[1], "is located at index 1.")
print(food[2], "is located at index 2.")
#print(food[3], "is located at index 3") - displays an index error in food list - index out of range

print(food[-1], "is located at index -1") # prints the last element of the list, food

if ("Sundae" in food):
  print("One sundae, coming up!")
else:
  print("Sorry, we don't carry sundaes!")
  
if ("Shake" in food):
  print("One shake, coming up!")
else:
  print("Sorry, No shakes available!")
  
if ("Fries" in food):
  print("Fries coming up!")
else:
  print("Sorry, No fries available!")
  
if ("Burger" in food):
  print("Burgers are comming up!")
else:
  print("Sorry, No burgers available!")
  
if ("Pizza" in food):
  print("Pizzas are comming up!")
else:
  print("Sorry, No pizzas available!")
  