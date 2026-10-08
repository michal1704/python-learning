age = int(input("How old are you?"))
ticket = input("Do you have a ticket?")

if age >= 15 and ticket == "yes":
    print("You can enter.")
else:
    print("Access denied.")

print()

age = int(input("How old are you? "))
has_license = input("Do you have a driving license? ")

if age >= 18 and has_license == "yes":
    print("You can drive.")
else:
    print("You cannot drive.")

print()
age = int(input("How old are you? "))
if age < 13:
    print("Child ticket")
elif age < 18:
    print("Teen ticket")
elif age < 65:
    print("Adult ticket")
else:
    print("Senior ticket")

print()
age = int(input("How old are you? "))
has_ticket = input("Do you have a ticket? ")

if age < 15:
    print("Too young")
elif has_ticket == "yes":
    print("You can enter.")
else:
    print("You need a ticket")
print()

price = int(input("What is the price? "))
is_member = input("Are you a member? ")

if price < 500:
    print("standard price")
elif is_member == "yes":
    print("You get a discount")
else:
    print("No discount")
print()

price = int(input("What is the price? "))
quantity = int(input("How many do you want? "))

if price * quantity >= 1000:
    print("Free shipping")
else:
    print("Shipping costs 100")

price = 300
quantity = 4 

total_price = price * quantity

print("Total price:", total_price)

if total_price >= 1000:
    print("Free shipping")
else:
    print("Shipping costs 100")
print()

price = int(input("Price: "))
quantity = int(input("Quantity: "))
is_member = input("Are you a member? ")

total = price * quantity
if total >= 1000 and is_member == "yes":
    print("you get a discount")
else:
    print("No discount")

print("Total price:", total)

print()

balance = 5000
withdraw = int(input("How much do you want to withdraw? "))

if balance >= withdraw:
    print("Withdrawal successful")
    new_balance = balance - withdraw
    print("New balance:", new_balance)
else:
    print("Insufficient funds")

