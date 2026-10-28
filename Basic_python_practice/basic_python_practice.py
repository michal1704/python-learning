
temperature = 7 

if temperature < 10:
    print("It's cold outside.")
else:
    print("It's warm outside.")
print()
age = 16 

if age < 13:
    print("child")
elif age < 18:
    print("teenager")
else:
    print("adult")
print()
score = 72

if score < 50:
    print("fail")
elif score < 70:
    print("pass")
elif score < 90:
    print("good")
else:
    print("excellent")

print()
names = ["Anna", "Petr", "Eva"]

for name in names:
    print(name)
print()

scores = [45, 72, 91, 63]

for score in scores:
    if score < 50:
        print("fail")
    elif score < 70:
        print("pass")
    elif score < 90:
        print("good")
    else:
        print("excellent")
print()
temperatures = [5, 18, 27, 9]

for temperature in temperatures:
    if temperature < 10:
        print("It's cold outside.")
    elif temperature < 20:
        print("It's mild outside.")
    else:
        print("It's warm outside.")
print()
age = 18

print (age == 18)
print()
age = 16

print (age == 18)
print()
name = "Petr"
if name == "Petr":
    print("Ahoj, Petře!")
print()
password = "python123"

if password == "python123":
    print("Access granted.")
else:
    print("Access denied.")
print()
username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Access granted.")
else:
    print("Access denied.")
print()

status = "student"
if status == "student" or status == "senior":
    print("Discount")
else:
    print("No discount")
print()

age = int(input("how old are you? "))

if age < 13:
    print("You are a child.")
    print("Access denied.")
elif age < 18:
    print("You are a teenager.")
    print("Access denied.")
else:
    print("You are an adult.")
    print("Access granted.")
    print("Welcome to the system!")

print()
print(type(18))
print(type("18"))
print(10+5)
print()

money = 1000
price = 600

price = int(input("Price:"))
money = int(input("How much money do you have? "))

if money >= price:
    left = money - price
    print("You can buy it.")
    print("You will have", left, "left.")
else:
    print("You don't have enough money.")
