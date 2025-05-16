# this is a function definition
def print_hello():
  print("hello world")
  
# this is a call of that function
print_hello()

# this function takes two arguments and returns their sum
def add(operand1, operand2):
  return operand1 + operand2
  
# since the add function returns a value it must be stored
# somewhere
sum = add(2, 3)

# that value isn't printed unless you use a print statement
print(sum)