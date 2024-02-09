import os

def main():
    print("Open your shop simulator")
    print("1. New Item")
    print("2. Sell Item")
    print("3. Check money")
    print("4. Item List")
    
money = 0
item = {}

while True:
    main()
    chc = input("Enter your choice: ")
    if chc == "1":
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            new_item = str(input("Enter your item name: "))
            if new_item == "":
                print("Invalid item name!")
                input("Press Enter to continue!")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                new_price = int(input("Enter your the price of your item: "))
                item[new_item] = new_price
                input("Successfuly created! Press Enter to continue")
                os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            print("Invalid Price!")
            input ("Press Enter to continue")
            os.system('cls' if os.name == 'nt' else 'clear')
    elif chc == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        sell = input("Enter the name of the item: ")
        if sell in item:
            money += item[sell]
            print("Successfuly selled! for $", item[sell])
            input("Press Enter to continue")
        else:
            print("Invalid item name!")
            input("Press Enter to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif chc == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Your money: $", money)
        input("Press Enter to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif chc == "4":
        if item:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Item list:")
            for myitem, price in item.items():
                print(f"{myitem.capitalize()} : ${price}")      
                input("Press Enter to continue")
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("You don't have any items yet!")
            input("Press Enter to continue")
            os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Invalid choice!")
        input("Press Enter to continue")
        os.system('cls' if os.name == 'nt' else 'clear')