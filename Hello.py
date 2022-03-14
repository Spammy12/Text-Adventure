a = 0
b = "look, eat, jump"
#This runs a check on the name and will cycle until the name is not an empty space or number.
while a < 1: 
    name = input("Type Your Name Here: ")
    if len(name.lower()) == 0 or name.isdigit():
        print("Please enter a real name")
    else:
        print ("Your name is " + name + ".")
        a = 1

a = 0 #This will allow the text to continue cycling until an option is reached.larr
print("You see a room.")
while a < 1:
    choice = input("What now? ")
    if choice == "help":
        print("Current commands are " + b + ". Oh, and quit.")
    elif choice in "look, eat, jump":
        if choice == "look":
            print("You are standing in an empty room. Well... except the wizard")
        elif choice == "eat":
            print("You are feeling a little hungry, but you have nothing you can eat.")
        elif choice == "jump":
            print("Yippee!")
    elif choice == "quit":
        print("Oh, okay then. Goodbye!")
        input()
        a = 1
    else:
        print("That is not possible. Type help for a list of commands.")
