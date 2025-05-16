# Combo Menu
total_cost = 0 # set the total cost to be 0

# setup a list for the order
order = []

# Added a while True loop
while True:
    # Resetted the order
    selected_a_sandwich = True # set the variable selected_a_sandwich to be true
    selected_a_beverage = True # set the variable selected_a_beverage to be true
    selected_french_fries = True # set the variable selected_a_beverage to be true
    
    # Ask the user for a sandwich type with a user input: Chicken - $5.25, Beef - $6.25, Tofu - $5.75, none
    sandwich = input("What type of sandwich would you like? Chicken for $5.25, Beef for $6.25, Tofu for $5.75, or none? ")

    # If the user types a type of sandwich:
    # Determine the sandwich cost
    sandwich_cost = 0

    if sandwich == "chicken":
        # the list will add a chicken sandwich to your order
        order.append("chicken")
        sandwich_cost += 5.25
    elif sandwich == "beef":
        # the list will add a beef sandwich to your order
        order.append("beef")
        sandwich_cost += 6.25
    elif sandwich == "tofu":
        # the list will add a tofu sandwich to your order
        order.append("tofu")
        sandwich_cost += 5.75
    # It displays no sandwich selected if the user enters none. 
    elif sandwich == "none":
        # the list will add no sandwich to your order and the variable selected_a_sandwich will be false
        order.append("no sandwich")
        sanwich_cost = 0
        print("No sandwich selected.")
        selected_a_sandwich = False
    # It displays invalid sandwich choice, no sandwich added if nothing entered or not typed correctly  in sandwich type field.
    else:
        """ if it is an invalid sandwich choice then no sandwich will be added to your order 
        then the variable selected_a_sandwich will be false"""
        print("Invalid sandwich choice, no sandwich added.")
        order.append("no sandwich") 
        selected_a_sandwich = False
        
    # Display the sandwich type using the following print statement : "You ordered a " + sandwich + " sandwich."
    print(f"You ordered a {sandwich} sandwich.")

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
                # the order will append large fry size
                order.append("large fry size")
                fries_cost += 2.00
            # If the user inputs no
            else:
                # Fries cost would be $1 and the order will append a small fry size
                order.append("small fry size")
                fries_cost += 1.00

        elif fry_size == "medium":
            # Fries cost would be $1.50 and the order will append a medium fry size
            order.append("medium fry size")
            fries_cost += 1.50

        elif fry_size == "large":
            # Fries cost would be $2.00 and the order will append a large fry size
            order.append("large fry size")
            fries_cost += 2.00
        
        else:
            # If the user types it incorrectly then it will say invalid size no fries added.
            print("Invalid french fry size, no fries added.")
            # the order will append no fries and the variable selected_french_fries will be False
            order.append("no fries")
            selected_french_fries = False
            

        print(f"You selected {fry_size} fries." if fries_cost > 0 else "No fries added")
    # If the user says no it says no fries selected.
    else:
        # the order will append no fries and the variable selected_french_fries will be False
        selected_french_fries = False
        order.append("no fries")
        fries_cost = 0
        print("No fries selected.")


    # Ask the user for a beverage with a user input
    beverage = input("Would you like a beverage? (yes/no) ")
    beverage_cost = 0

    # If the user says yes 
    if beverage == "yes":
        size = input("What size of beverage would you like? small $1.00, medium $1.50, large $2.00 ")
        if size == "small":
            # the order will append small beverage size and the cost will be $1
            order.append("small beverage")
            beverage_cost += 1
        elif size == "medium":
            # the order will append medium beverage size and the cost will be $1.50
            order.append("medium beverage")
            beverage_cost += 1.50
        elif size == "large":
            # the order will append large beverage size and the cost will be $2
            order.append("large beverage")
            beverage_cost += 2
        # If nothing entered or not typed correctly in beverage field, it displays invalid beverage size, no beverage added.
        else:
            # the order will append no beverage
            print("Invalid beverage size, no beverage added.")
            order.append("no beverage")
            selected_a_beverage = False
        print("You selected a " + size + " beverage." if beverage_cost > 0 else "No beverage added.")
    else:
        # the order will append no beverage and the beverage cost will be $0
        print("No beverage selected.")
        order.append("none")
        beverage_cost = 0
        selected_a_beverage = False

    # Calculate and display the total cost
    # Simplified the total cost calculation
    total_cost = sandwich_cost + beverage_cost + fries_cost
    if total_cost == 0:
        # If the user ordered nothing then the no order message displays
        print(f"You have ordered nothing, your total cost is ${total_cost:.2f}")
    else:
        print(f"Your total cost is ${total_cost:.2f}")
        
    print("Order Summary: {}".format(order))
    
    another_order = input("Would you like to place another order? (yes/no): ")
    
    # Added a break statement if the user says no
    if another_order != "yes":
        break

# A thank you message displays after the user is finished placing all their orders
print("Thank you for your order")


