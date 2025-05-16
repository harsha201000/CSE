# HarshaMalipeddi
#Activity 3.2.2 Step 7
from Post import Post

all_posts_archive = []

# your code here
username = input("Enter a username: ")
print("Welcome {}".format(username))

user_input = input("""What would you like to do?: 
new - Add a post to the archive
remove - Remove a post from the archive
change user - Change their username associated with future posts
print - Display the current, up-to-date list of all posts
quit - End the program 
""")

# This while loop ensures that the program will continue executing 
# statements at the next indentation level until the user types "quit" 
# in response to the prompt.
while user_input != "quit":

    # code for adding a post here
    if user_input == 'add':
      message = input('What would you like to post?')
      new_Post = Post(username,message)
      all_posts_archive.append(new_Post)
      print("Post added!")
    # code for removing a post here
    elif user_input == "remove":
        if not all_posts_archive:
            print("No posts to remove!")
        else:
            print("\nHere are the posts:")
            for i, post in enumerate(all_posts_archive):
                print(f"{i}: {post.user_name} - {post.message}")  # Display posts with index

            try:
                index_input = input("\nEnter the index of the post to remove: ").strip()
                if index_input.isdigit():  # Ensure input is a number
                    index = int(index_input)
                    if 0 <= index < len(all_posts_archive):  # Check if index is within range
                        removed_post = all_posts_archive.pop(index)  # Remove the selected post
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
      for post in all_posts_archive:
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
  