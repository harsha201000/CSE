# HarshaMalipeddi
assignment=" "
def assignment1():
  print("Assignment 1 Completed!")
  
def assignment2():
  print("Assignment 2 Completed!")

def execute_assignment(assignment):
  while assignment != "quit":
    assignment = input("Enter assignment ")
    if assignment == "1":
      print("Assignment 1 Completed!")
    elif assignment == "2":
      print("Assignment 2 Completed!")
    elif assignment == "quit":
      print("All done")
      break
    
execute_assignment(assignment)




