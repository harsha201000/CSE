my_list = [0,1,2] 
for number in my_list: 
  print (number)
  
x = 0 
my_list = [0,1,2] 
for number in my_list: 
  x = x + number 

print (x)

# [0,1,2,3,4,5,6]
a = range(7)
a = list(a) 
print(a)

# [1,2,3,4,5,6,7]
a = range(1,8)
a = list(a) 
print(a)

# [0,5,10,15,20,25,30,35]
a = range(0,40,5)
a = list(a) 
print(a)

# [0,3,6,9,12,15]
a = range(0,16,3)
a = list(a) 
print(a)

# [0,-2,-4,-6,-8]
a = range(0,-10,-2)
a = list(a)
print(a)

# [ ]
a = range(0)
a = list(a)
print(a)

# [ ]
a = range(0)
a = list(a)
print(a)

print("Numbers 1 to 19 inclusive")
for i in range(1,20):
  print(i)
  
print("Numbers 20 to 1 inclusive")
for i in range(20,0,-1):
  print(i)
  
print("Even numbers from 2 to 10 inclusive")
for i in range(2,12,2):
  print(i)
  
print("Odd numbers from 9 to 1 inclusive")
for i in range(9,-1,-2):
  print(i)

print("the numbers from 1 up to 5 inclusive")
i = 1
while i <= 5:
  print(i)
  i += 1
  
print("the numbers from 10 down to 1 inclusive")
i = 10
while i >= 1:
  print(i)
  i -= 1
  
print("the even numbers from 2 to 10 inclusive using the mod operator and a conditional")
i = 2
while i <= 10:
  if i % 2 == 0:
    print(i)
  i += 2
  
print("the odd numbers from 9 to 1 inclusive using the mod operator and a conditional")
i = 9
while i >= 1:
  if i % 2 != 0:
    print(i)
  i -= 1

