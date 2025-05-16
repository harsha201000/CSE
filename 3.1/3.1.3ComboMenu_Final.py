# Iteration 4 - Final

# Ask the user for a sandwich type with a user input: Chicken - $5.25, Beef - $6.25, Tofu - $5.75, none
sandwich = input("What type of sandwich would you like? Chicken for $5.25, Beef for $6.25, Tofu for $5.75, or none? ")

# If the user types a type of sandwich:
# Determine the sandwich cost
sandwich_cost = 0

if sandwich == "chicken":
    sandwich_cost = 5.25
elif sandwich == "beef":
    sandwich_cost = 6.25
elif sandwich == "tofu":
    sandwich_cost = 5.75
# It displays no sandwich selected if the user enters none. 
elif sandwich == "none":
    print("No sandwich selected.")
# It displays invalid sandwich choice, no sandwich added if nothing entered or not typed correctly  in sandwich type field.
else:
    print("Invalid sandwich choice, no sandwich added.")
    
# Display the sandwich type using the following print statement : "You ordered a " + sandwich + " sandwich."
print(f"You ordered a {sandwich} sandwich." if sandwich != "none" else "No sandwich selected.")

# Ask the user for french fries with a user input
fries = input("Would you like french fries? (yes/no) ")
fries_cost = 0

# If the user says yes
if fries == "yes":
    # ask what size would they like: small - $1.00, medium - $1.50, large - $2.00
    fry_size = input("What size of french fries would you like? small - $1.00, medium - $1.50, large - $2 ")
    # If the user says small
    if fry_size == "small":
        # Ask the user for a megasize for their fries
        mega_size = input("Would you like to mega-size your fries to large? (yes/no) ")
        # If the user inputs yes
        if mega_size == "yes":
            # Give them large fries at the large fries price instead of the small fries price
            fry_size = "large"
            fries_cost = 2.00
        # If the user inputs no
        else:
            # Fries cost would be $1
            fries_cost = 1.00

    elif fry_size == "medium":
        fries_cost = 1.50

    elif fry_size == "large":
        fries_cost = 2.00
    
    else:
        # If the user types it incorrectly then it will say invalid size no fries added.
        print("Invalid french fry size, no fries added.")

    print(f"You selected {fry_size} fries." if fries_cost > 0 else "No fries added")
# If the user says no it says no fries selected.
else:
    print("No fries selected.")


# Ask the user for a beverage with a user input
beverage = input("Would you like a beverage? (yes/no) ")
beverage_cost = 0

# If the user says yes 
if beverage == "yes":
    size = input("What size of beverage would you like? small $1.00, medium $1.50, large $2.00 ")
    if size == "small":
        beverage_cost = 1
    elif size == "medium":
        beverage_cost = 1.50
    elif size == "large":
        beverage_cost = 2
    # If nothing entered or not typed correctly in beverage field, it displays invalid beverage size, no beverage added.
    else:
        print("Invalid beverage size, no beverage added.")
    print("You selected a " + size + " beverage." if beverage_cost > 0 else "No beverage added.")
else:
    print("No beverage selected.")

# Calculate and display the total cost

""" Use Boolean Operators, if/else, elif and variables to determine a total on the order if you ordered all three, 
if you order only two of the three if you ordered only one of the three, etc. """
if sandwich == "chicken" or sandwich == "beef" or sandwich == "tofu" and beverage == "yes" and fries == "yes":
    total_cost = sandwich_cost + beverage_cost + fries_cost
    print(f"Your total cost is ${total_cost:.2f}")

elif sandwich == "none" and beverage == "yes" and fries == "yes":
    total_cost = sandwich_cost + beverage_cost + fries_cost
    print(f"Your total cost is ${total_cost:.2f}")

elif sandwich == "none" and beverage == "no" and fries == "yes":
    total_cost = sandwich_cost + beverage_cost + fries_cost
    print(f"Your total cost is ${total_cost:.2f}")

elif sandwich == "none" and beverage == "yes" and fries == "no":
    total_cost = sandwich_cost + beverage_cost + fries_cost
    print(f"Your total cost is ${total_cost:.2f}")

elif sandwich == "none" and beverage == "no" and fries == "no":
    total_cost = sandwich_cost + beverage_cost + fries_cost
    print(f"Your total cost is ${total_cost:.2f}")

elif sandwich == "chicken" or sandwich == "beef" or sandwich == "tofu" and beverage == "yes" and fries == "no":
    total_cost = sandwich_cost + beverage_cost + fries_cost
    print(f"Your total cost is ${total_cost:.2f}")

elif sandwich == "chicken" or sandwich == "beef" or sandwich == "tofu" and beverage == "no" and fries == "yes":
    total_cost = sandwich_cost + beverage_cost + fries_cost
    print(f"Your total cost is ${total_cost:.2f}")

elif sandwich == "chicken" or sandwich == "beef" or sandwich == "tofu" and beverage == "no" and fries == "no":
    total_cost = sandwich_cost + beverage_cost + fries_cost
    print(f"Your total cost is ${total_cost:.2f}")

elif sandwich == "none" and beverage == "no" and fries == "no":
    total_cost = sandwich_cost + beverage_cost + fries_cost
    print(f"You have ordered nothing, Your total cost is ${total_cost:.2f}")
# If the user types something incorrectly or random letters and words
else:
    print("Your order is invalid, please try again!!!")