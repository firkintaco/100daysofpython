print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
hinta = 0
# Määritellään hinta koon mukaan
if size == "S":
    hinta += 15
    if add_pepperoni == "Y":
        hinta += 2
elif size == "M":
    hinta += 20
    if add_pepperoni == "Y":
        hinta += 3
elif size == "L":
    hinta += 25
    if add_pepperoni == "Y":
        hinta += 3

if extra_cheese == "Y":
    hinta += 1

print(f"Your final bill is: ${hinta}")
