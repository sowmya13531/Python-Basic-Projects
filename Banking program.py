#Python Banking Program
def showbalance(balance):
    print("****************************")
    print(f"Your balance is ${balance:.2f}")
    print("****************************")
def deposit():
    print("****************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("****************************")
    if amount < 0:
        print("Invalid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    print("****************************")
    amount = float(input("Enter withdrawl amount: "))
    print("****************************")
    if amount > balance:
        print("Insufficient Amount")
        return 0
    elif amount < 0:
        print("Amount atleast to be 1")
        return 0
    else:
        return amount
def main():
    balance = 0
    is_running = True
    while is_running:
        print("************************")
        print("      Banking pro         ")
        print("1.Show Balance")
        print("Deposit Amount")
        print("Withdrawl amount")
        print("Exit")
        choice = input("ENter your choice (1-4): ")
        if choice == "1":
         showbalance(balance)
        elif choice == "2":
         balance += deposit()
        elif choice == "3":
         balance -= withdraw(balance)
        elif choice == "4":
         is_running = False
        else:
         print("****************************")
         print("That is not valid choice")
         print("****************************")
    print("****************************")
    print("Tq have a great day")
    print("****************************")
if __name__ == '__main__':
    main()
