print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
if size == "S":
    pizza_cost = 15
elif size == "M":
    pizza_cost = 20
elif size == "L":
    pizza_cost = 25
else:
    print("Invalid choice. Please select a valid pizza size.")
    exit()

# Add pepperoni cost
if size == "S" and add_pepperoni == "Y":
    pizza_cost += 2
elif (size == "M" or size == "L") and add_pepperoni == "Y":
    pizza_cost += 3

# Add extra cheese cost
if extra_cheese == "Y":
    pizza_cost += 1

print(f"Your final bill is: ${pizza_cost}.")
