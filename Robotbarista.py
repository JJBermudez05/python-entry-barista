#Build a Robot Barista!!

print("Hello, welcome to Caffeine Dreams!")

name = input("What is your name?\n")


print("Hello " + name + ", thank you so much for coming in today!\n")

menu = "Black Coffee, Espresso, Latte, Cappuccino"  

print(name + ", what would you like from our menu today? Here is what we are serving.\n"
+ menu )

order = input()

price = 6

quantity = input("How many coffee would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print(name + ", we'll have your " + quantity +  " "  + order + " ready for you in a moment.")










