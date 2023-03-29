from client import Client
from bank import Bank


bank = Bank()
print()
print("Welcome to {}!".format(bank.name))
print()
running = True
while running:
    print()
    print("""Choose a banking option:

    1. Open a new bank account
    2. Open an existing bank account
    3. Exit
    """)

    choice = int(input("1, 2 or 3: "))

    if choice == 1:
        print()
        print("For creation of an account, Please fill in the information below.")
        print()
        client = Client(input("Name: "), int(input("Deposit amount: ")))
        bank.update_db(client)
        print()
        print("Your Account has been created successfully! Your account number is: ", client.account['account_number'])
    elif choice == 2:
        print()
        print("For accessing your account, Please enter your credentials below.")
        print()
        name = input("Name: ")
        account_number = int(input("Account number: "))
        current_client = bank.authentication(name, account_number)
        if current_client:
            print()
            print("Welcome {}!".format(current_client.account['name']))
            acc_open = True
            while acc_open:
                print()
                print("""Choose an option:

    1. Withdraw of money
    2. Deposit of money
    3. Balance inquiry
    4. Exit
    5. Transfer to other account
                    """)
                acc_choice = int(input("1, 2, 3 ,4 or 5: "))
                if acc_choice == 1:
                    print()
                    current_client.withdraw(int(input("Withdrawn amount: ")))
                elif acc_choice == 2:
                    print()
                    current_client.deposit(int(input("Deposited amount: ")))

                elif acc_choice == 3:
                    print()
                    current_client.balance()
                elif acc_choice == 4:
                    print()
                    print("Thank you for visiting ABC Bank!")
                    current_client = ''
                    acc_open = False
                elif acc_choice == 5:
                    print("State the amount that needs to be transferred from another bank account")
                    transfer_account = int(input("Enter account number to be transferred from"))
                    current_client.transfer(int(input("transferred amount: ")))
        else:
            print()
            print("Authentication process has failed!")
            print("Reason: account not found/ Invalid Credentials.")
            continue
    elif choice == 3:
        print()
        print("Thank You for Banking with us!")
        running = False