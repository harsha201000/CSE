"""
This program is intended as a tracer round for the flow of control as 
a user of a social media account makes, deletes, and edits posts. For 
testing, a user should be able to enter their user name, change which 
user name they are currently using, add a post using their current user 
name, remove a post made under their current user name, edit a post 
made under their current user name, print the contents of the list of 
posts, or quit the program.
"""

# This line of code tells the Python interpreter that it needs to 
# reference the post.py file in order to run the rest of the code 
# in this file.
from Post import Post

# How will you save the posts you will create? Review the for loop 
# near the end of this code for an answer.
post_list = [ ]

# What is the user name they want to use?
username = input("Hello, What is your name?")

# Welcome user to the program
print("Hello {}, Welcome!".format(username))

# Store initial user input in a variable identified by user_input

# You may need to use this statement again to complete the activity.

user_input = input(""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

""")


# This while loop ensures that the program will continue executing 
# statements at the next indentation level until the user types "quit" 
# in response to the prompt.
while user_input != "quit":

    # code for adding a post here
    if user_input == 'add':
      message = input('What would you like to post?')
      new_Post = Post(username,message)
      post_list.append(new_Post)
      print("Post added!")
    # code for removing a post here
    elif user_input == "remove":
        if not post_list:
            print("No posts to remove!")
        else:
            print("\nHere are the posts:")
            for i, post in enumerate(post_list):
                print(f"{i}: {post.user_name} - {post.message}")  # Display posts with index

            try:
                index_input = input("\nEnter the index of the post to remove: ").strip()
                if index_input.isdigit():  # Ensure input is a number
                    index = int(index_input)
                    if 0 <= index < len(post_list):  # Check if index is within range
                        removed_post = post_list.pop(index)  # Remove the selected post
                        print(f"Post '{removed_post.message}' removed!")
                    else:
                        print("Invalid index! Please enter a valid number from the list.")
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("An error occurred. Try again!")

            
    # code for changing the current user here
    elif user_input == 'change user':
        username = input("Enter new username: ")
        print("Username changed to {}!".format(username))
    # code to display all posts, you can use the code in comments below
	  # this for loop will print the list
	  # and the element itself
    elif user_input == 'print':
      index = 0
      for post in post_list:
        print (str(index), ":", post)
        index += 1
    
    # code to inform the user that their input was not valid here
    else:
      print("Invalid input!!!")
    
# code that will allow the user to make a new selection
    user_input = input(""" What would you want to do now?
    "add" - Add a post to the archive
    "remove" - Remove a post from the archive
    "change user" - Change the user name associated with any future posts
    "print" - Display the current up to date list of all posts
    "quit" - End the program

    """)
# This code will finish the loop