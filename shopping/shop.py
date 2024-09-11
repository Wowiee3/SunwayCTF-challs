coins = 20;
bag = []

def menu():
    print("\nWelcome to the store! Feel free to buy and sell whatever you like!");

    print("You have", coins, "coins.");
    print("-----------------");
    print("[1] Buy apples (10 coins)");
    print("[2] Buy flag (100 coins) \n");

    global choice
    choice = input("Enter your choice: ");

    if choice == "1":
        apple()
    elif choice == "2":
        flag()
    else:
        print("Invalid choice.")

def apple():
    amount = int(input("How many apples do you want to buy?: "))
    global coins
    if coins >= 10 * amount:
        for x in range(amount):
            bag.append("Apple")
        coins -= 10 * amount
        print("Items in bag: ")
        for i in bag:
            print("-", i)
    else:
        print("You don't have enough coins for that!")
    menu()

def flag():
    amount = int(input("How many flags do you want to buy?: "))
    global coins
    if coins >= 100 * amount:
        print("Here's your flag!: sunctf{til_you_dr0p}")
    else:
        print("You don't have enough coins for that!")
        menu()

menu()
