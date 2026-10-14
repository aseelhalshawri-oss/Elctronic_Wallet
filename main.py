import os
import getpass
from database import Database
from user import User
from wallet import Wallet
from wallet_currency import Wallet_currency
from currency import Currency
from transaction import Transaction
from beneficiary import Beneficiary
from notification import Notification
from notification_details import Notification_details



# -----------------------------------
db = Database()
# -----------------------------------

def clear_screen():
    os.system("cls")

# -----------------------------------
def Users_Management(db):
    while True:
        print("\n-----Users Management-----")
        print("-" * 40)
        print("1- Add User")
        print("2- View All the Users")
        print("3- search for a user")
        print("4- Update data of user")
        print("5- Delete the user")
        print("0- to back")
        print()
        print("-" * 40)

        user_choice = int(input("Choose number from Users Management : "))
    
        clear_screen()

        if user_choice == 1:
            print("\n-----Add New User-----")
            fname = input("Enter First Name : ")
            mname = input("Enter Mid Name : ")
            lname = input("Enter Last Name : ")
            phone = int(input("Enter Phone Number : "))
            email = input("Enter your Email : ")
            password = getpass.getpass("Enter your password: ")
            dob = input("Enter your Date of birth : ")
            new_user = User(fname, mname, lname, phone, email, password, dob)
            new_user.add_user(db)

        elif user_choice == 2:
            print("-----All The Users-----")
            users = User.view_all(db)
            for row in users:
                print("=" * 30)
                print(f"user id          : {row[0]}")
                print(f"Full_Name        : {row[1]} {row[2]} {row[3]}")
                print(f"Phone Number     : {row[4]}")
                print(f"Email            : {row[5]}")
                print(f"Password         : {row[6]}")
                print(f"Date_of_Birth    : {row[7]}")
                print(f"Created_At       : {row[8]}")
                print("=" * 30)

        elif user_choice == 3:
            print("search by first name for view information user : ")
            fname = input("Enter First Name : ")
            result = User.search_by_firstName(db, fname)
            if result:
                print("found it ")
                for row in result:
                    print("=" * 30)
                    print(f"user id          : {row[0]}")
                    print(f"Full_Name        : {row[1]} {row[2]} {row[3]}")
                    print(f"Phone Number     : {row[4]}")
                    print(f"Email            : {row[5]}")

                    print("=" * 30)
            else:
                print("No founded with this name")

        elif user_choice == 4:
            print("------Update password of user------")
            id = int(input("Enter User id : "))
            new_password = input("Enter New Password : ")
            User.update_password(db, id, new_password)

        elif user_choice == 5:
            print("-----Dlete User-----")
            id = int(input("Enter User id : "))
            confirm = input("Are you sure ? y,n : ")
            if confirm == "y":
                User.delete_user(db, id)
            elif confirm == "n":
                print("Deleted failed ")

        elif user_choice == 0:
            break

        else:
            print("The number that you chose is wrong !!!")

# ------------------------------------
def Wallets_Management(db):
    while True:
        print("\n-----Wallets Management-----")
        print("-" * 40)
        print("1- Add wallet")
        print("2- View All the wallets")
        print("3- search by wallet_id")
        print("4- Update status of wallet")
        print("5- Delete the wallet")
        print("0- to back")
        print()
        print("-" * 40)

        wallet_choice = int(input("Choose number from Wallets Management : "))

        clear_screen()

        if wallet_choice == 1:
            print("\n-----Add New wallet-----")
            user_id = int(input("Enter user id : "))
            status = input("Enter wallet status (Active or UnActive) : ")
            new_wallet = Wallet(user_id, status)
            new_wallet.add_wallet(db)

        elif wallet_choice == 2:
            print("-----All The Wallets-----")
            wallets = Wallet.view_all(db)
            for row in wallets:
                print("=" * 30)
                print(f"Wallet id        : {row[0]}")
                print(f"user id          : {row[1]}")
                print(f"wallet status    : {row[2]}")
                print(f"Created At       : {row[3]}")
                print("=" * 30)

        elif wallet_choice == 3:
            print("search by wallet id for view information wallet : ")
            wallet_id = int(input("Enter wallet id : "))
            result = Wallet.search_by_wallet_id(db, wallet_id)
            if result:
                print("found it ")
                print("=" * 30)
                print(f"Wallet id        : {result[0]}")
                print(f"user id          : {result[1]}")
                print(f"wallet status    : {result[2]}")
                print(f"Created At       : {result[3]}")
                print("=" * 30)
            else:
                print("No founded with this name")

        elif wallet_choice == 4:
            print("------Update status of wallet------")
            wallet_id = int(input("Enter wallet id : "))
            new_status = input("Enter wallet status (Active or UnActive) : ")
            Wallet.update_status(db, wallet_id, new_status)

        elif wallet_choice == 5:
            print("-----Dlete wallet-----")
            wallet_id = int(input("Enter wallet id : "))
            confirm = input("Are you sure ? y,n : ")
            if confirm == "y":
                Wallet.delete_wallet(db, wallet_id)
            elif confirm == "n":
                print("Deleted failed ")

        elif wallet_choice == 0:
            break

        else:
            print("The number that you chose is wrong !!!")

# ------------------------------------
def Wallet_Currency_Management(db):
    while True:
        print("\n-----Wallets currency Management-----")
        print("-" * 40)
        print("1- Add wallet currency")
        print("2- View All the wallets currency")
        print("3- search by wallet_id")
        print("4- update balance for wallet currency")
        print("5- delete wallet currency")
        print("0- to back")
        print()
        print("-" * 40)

        wallet_cur_choice = int(
            input("Choose number from Wallets currency Management : ")
        )

        clear_screen()

        if wallet_cur_choice == 1:
            print("\n-----Add New wallet currency-----")
            wallet_id = int(input("Enter wallet id : "))
            currency_id = int(input("Enter currency id (1 YER , 2 SAR , 3 USD) : "))
            balance = float(input("Enter the balance : "))
            new_wallet_currency = Wallet_currency(wallet_id, currency_id, balance)
            new_wallet_currency.add_wallet_currency(db)

        elif wallet_cur_choice == 2:
            print("-----All The Wallets currency-----")
            wallets_cur = Wallet_currency.view_all(db)
            for row in wallets_cur:
                print("=" * 30)
                print(f"Wallet currency id  : {row[0]}")
                print(f"currency id         : {row[1]}")
                print(f"wallet id           : {row[2]}")
                print(f"the balance         : {row[3]}")
                print("=" * 30)

        elif wallet_cur_choice == 3:
            print("search by wallet id for view information wallets_currency : ")
            wallet_id = int(input("Enter wallet id : "))
            result = Wallet_currency.search_by_wallet_id(db, wallet_id)
            if result:
                print("found it ")
                for row in result:
                    print("=" * 30)
                    print(f"Wallet  id          : {row[0]}")
                    print(f"first_name          : {row[1]}")
                    print(f"Wallet currency id  : {row[2]}")
                    print(f"currency code       : {row[3]}")
                    print(f"the balance         : {row[4]}")
                    print("=" * 30)
            else:
                print("No founded with this name")


        elif wallet_cur_choice == 4:
            print("------Update balance of wallet currency------")
            wallet_currency_id = int(input("Enter wallet currency id : "))
            new_balance = int(input("Enter new balance  : "))
            Wallet_currency.update_balance(db, new_balance, wallet_currency_id)


        elif wallet_cur_choice == 5:
            print("-----Dlete wallet currency-----")
            wallet_currency_id = int(input("Enter wallet currency id : "))
            confirm = input("Are you sure ? y,n : ")
            if confirm == "y":
                Wallet_currency.delete_wallet_currency(db, wallet_currency_id)
            elif confirm == "n":
                print("Deleted failed ")

        elif wallet_cur_choice == 0:
            break

        else:
            print("The number that you chose is wrong !!!")

# ------------------------------------
def Currency_Management(db):
    while True:
        print("\n-----Currency Management-----")
        print("-" * 40)
        print("1- Add currency")
        print("2- View All the currencies")
        print("3- search by currency_id")
        print("0- to back")
        print()
        print("-" * 40)

        currency_choice = int(input("Choose number from  currency Management : "))

        clear_screen()

        if currency_choice == 1:
            print("\n-----Add New currency-----")
            currency_name = input("Enter currency Name : ")
            currency_code = input("Enter currency code : ")
            new_currency = Currency(currency_name, currency_code)
            new_currency.add_currency(db)

        elif currency_choice == 2:
            print("-----All The  currencies-----")
            currency = Currency.view_all(db)
            for row in currency:
                print("=" * 30)
                print(f"currency id     : {row[0]}")
                print(f"currency Nmae   : {row[1]}")
                print(f"currency cod    : {row[2]}")
                print("=" * 30)

        elif currency_choice == 3:
            print("search by currency id for view information of currency : ")
            currency_id = int(input("Enter currency id : "))
            result = Currency.search_by_currency_id(db, currency_id)
            if result:
                print("found it ")
                print("=" * 30)
                print(f"currency id        : {result[0]}")
                print(f"currency Name      : {result[1]}")
                print(f"currency code      : {result[2]}")
                print("=" * 30)
            else:
                print("No founded with this name")

        elif currency_choice == 0:
            break

        else:
            print("The number that you chose is wrong !!!")

# ------------------------------------
def Transactions_Management(db):
    while True:
        print("\n-----Transactions Management-----")
        print("-" * 40)
        print("1- Add Transaction")
        print("2- View All the transactions")
        print("3- view all the information for sender and receiver")
        print("4- search by transaction id")
        print("5- update transaction status")
        print( "6- update balance just for transaction_status = (pending or failed) after update transaction_status")
        print("0- to back")
        print()
        print("-" * 40)

        transaction_choice = int(input("Choose number from Transactions Management : "))

        clear_screen()

        if transaction_choice == 1:
            print("\n-----Add New Transaction-----")
            sender_id = int(input("Enter sender_wallet_currency_id : "))
            receiver_id = int(input("receiver_wallet_currency_id : "))
            type = input("Enter transaction_type : ")
            status = input("Enter transaction_status : ")
            Amaunt = float(input("Enter transfer an Amount : "))
            desc = input("Enter transaction_desc: ")

            new_transaction = Transaction(sender_id, receiver_id, type, status, Amaunt, desc)
            new_transaction.add_transaction(db)

        elif transaction_choice == 2:
            print("-----View All the transactions-----")
            transactions = Transaction.view_all(db)
            for t in transactions:
                print("=" * 30)
                print(f"transaction id                  : {t[0]}")
                print(f"sender_wallet_currency_id       : {t[1]}")
                print(f"receiver_wallet_currency_id     : {t[2]}")
                print(f"transaction_type                : {t[3]}")
                print(f"transaction_status              : {t[4]}")
                print(f"Amount                          : {t[5]}")
                print(f"Created_At                      : {t[6]}")
                print(f"transaction_desc                : {t[7]}")
                print("=" * 30)

        elif transaction_choice == 3:
            print("view all the information for sender and receiver : ")
            results = Transaction.view_all_sc(db)
            if results:
                print("found it ")
                for row in results:
                    print("=" * 30)
                    print(f"transaction id       : {row[0]}")
                    print(f"sender_name          : {row[1]}")
                    print(f"receiver_name        : {row[2]}")
                    print(f"sender_currency      : {row[3]}")
                    print(f"receiver_currency    : {row[4]}")
                    print(f"Transfer an Amount   : {row[5]}")
                    print(f"operation type       : {row[6]}")
                    print(f"operation date       : {row[7]}")
                    print(f"sender balance       : {row[8]}")
                    print(f"receiver balance     : {row[9]}")
                    print("=" * 30)

        elif transaction_choice == 4:
            print("search by transaction id : ")
            trans_id = int(input("Enter transaction id : "))
            result = Transaction.search_by_transaction_id(db, trans_id)
            if result:
                print("found it")
                print("=" * 30)
                print(f"transaction id                  : {result[0]}")
                print(f"sender_wallet_currency_id       : {result[1]}")
                print(f"receiver_wallet_currency_id     : {result[2]}")
                print(f"transaction_type                : {result[3]}")
                print(f"transaction_status              : {result[4]}")
                print(f"Amount                          : {result[5]}")
                print(f"Created_At                      : {result[6]}")
                print(f"transaction_des                 : {result[7]}")
                print("=" * 30)
            else:
                print("No founded with this name")

        elif transaction_choice == 5:
            print("------update transaction status------")
            trans_id = int(input("Enter transaction id : "))
            new_status = input("Enter New status ('pending','completed','failed') : ")
            Transaction.update_status(db, new_status, trans_id)

        elif transaction_choice == 6:
            print("-----update balance after update transaction_status-----")
            trans_id = int(input("Enter transaction id : "))
            Transaction.update_balance_trans(db, trans_id)

        elif transaction_choice == 0:
            break

        else:
            print("The number that you chose is wrong !!!")

# ------------------------------------
def Beneficiary_Management(db):
    while True:
        print("\n-----Beneficiary Management-----")
        print("-" * 40)
        print("1- Add Beneficiary")
        print("2- View All the Beneficiary")
        print("3- search for a Beneficiary")
        print("4- Update data of Beneficiary")
        print("5- Delete the Beneficiary")
        print("0- to back")
        print()
        print("-" * 40)

        Beneficiary_choice = int(input("Choose number from Beneficiary Management : "))

        clear_screen()

        if Beneficiary_choice == 1:
            print("\n-----Add New Beneficiary-----")
            user_id = int(input("Enter user_id : "))
            beneficiry_name = input("Enter beneficiary Name : ")
            phone = int(input("Enter Phone Number : "))
            beneficiry_status = input(
                "Enter your beneficiary status(Active,UnActive) : "
            )
            new_beneficiary = Beneficiary(user_id, beneficiry_name, phone, beneficiry_status)
            new_beneficiary.add_beneficiary(db)

        elif Beneficiary_choice == 2:
            print("-----All The Beneficiary-----")
            beneficiary = Beneficiary.view_all(db)
            for row in beneficiary:
                print("=" * 30)
                print(f"beneficiary_id          : {row[0]}")
                print(f"user id                 : {row[1]}")
                print(f"beneficary_name         : {row[2]}")
                print(f"Phone Number            : {row[3]}")
                print(f"added                   : {row[4]}")
                print("=" * 30)

        elif Beneficiary_choice == 3:
            print("search by  name for view information Beneficiary : ")
            name = input("Enter Beneficiary Name : ")
            result = Beneficiary.search_by_Name(db, name)
            if result:
                print("found it ")
                for row in result:
                    print("=" * 30)
                    print(f"Beneficiary id            : {row[0]}")
                    print(f"user_id                   : {row[1]}")
                    print(f"Name                      : {row[2]}")
                    print(f"Phone Number              : {row[3]}")

                    print("=" * 30)
            else:
                print("No founded with this id")

        elif Beneficiary_choice == 4:
            print("------Update phone number of Beneficiary------")
            id = int(input("Enter Beneficiary id : "))
            new_phone = input("Enter New phone : ")
            Beneficiary.update_phone(db, id, new_phone)

        elif Beneficiary_choice == 5:
            print("-----Dlete Beneficiary-----")
            id = int(input("Enter Beneficiary id : "))
            confirm = input("Are you sure ? y,n : ")
            if confirm == "y":
                Beneficiary.delete_beneficiry(db, id)
            elif confirm == "n":
                print("Deleted failed ")

        elif Beneficiary_choice == 0:
            break

# ------------------------------------
def Notification_Management(db):
    while True:
        print("\n-----Notifications Management-----")
        print("-" * 40)
        print("1- Add Notifiction")
        print("2- View All the Notifications")
        print("3- search by Notification_id")
        print("0- to back")
        print()
        print("-" * 40)

        notification_choice = int(
        input("Choose number from  Notifications Management : "))

        clear_screen()

        if notification_choice == 1:
            print("\n-----Add New Notifiction-----")
            user_id = int(input("Enter user id : "))
            is_read = input("Enter  (readable,Unreadable) : ")
            massage = input("Enter the massage :")
            new_notification = Notification(user_id, is_read, massage)
            new_notification.add_notification(db)

        elif notification_choice == 2:
            print("-----All The Notifiction-----")
            notification = Notification.view_all(db)
            for row in notification:
                print("=" * 30)
                print(f"notifiction id     : {row[0]}")
                print(f"user id            : {row[1]}")
                print(f"is read            : {row[2]}")
                print(f"Date               : {row[3]}")
                print(f"massage            : {row[4]}")
                print("=" * 30)

        elif notification_choice == 3:
            print("search by notifiction id for view information of notifiction: ")
            notifiction_id = int(input("Enter notifiction id : "))
            result = Notification.search_by_notification_id(db, notifiction_id)
            if result:
                print("found it")
                print("=" * 30)
                print(f"notifiction id     : {result[0]}")
                print(f"user id            : {result[1]}")
                print(f"is read            : {result[2]}")
                print(f"Date               : {result[3]}")
                print(f"massage            : {result[4]}")
                print("=" * 30)
            else:
                print("No founded with this name")

        elif notification_choice == 0:
            break

        else:
            print("The number that you chose is wrong !!!")

# ------------------------------------
def Notification_details_Management(db):
    while True:
        print("\n-----Notifictions details Management-----")
        print("-" * 40)
        print("1- Add Notification details")
        print("2- View All the Notification details")
        print("3- search by reference_number")
        print("0- to back")
        print()
        print("-" * 40)

        notifiction_det_choice = int(
        input("Choose number from  Notifictions details Management : "))

        clear_screen()

        if notifiction_det_choice == 1:
            print("\n-----Add New Notifiction details-----")
            Transaction_id = int(input("Enter transaction id : "))
            reference_number = int(input("Enter  refernce number : "))
            commission = float(input("Enter the commission :"))
            new_notificaion_det = Notification_details(Transaction_id, reference_number, commission)
            new_notificaion_det.add_notification_detl(db)

        elif notifiction_det_choice == 2:
            print("-----All The Notifictions details-----")
            notifiction_det = Notification_details.view_all(db)

            for row in notifiction_det:
                print("found it")
                print("=" * 30)
                print(f"Notification id      : {row[0]}")
                print(f"Opration id          : {row[1]}")
                print(f"Sender Name          : {row[2]}")
                print(f"Receiver Name        : {row[3]}")
                print(f"Amount               : {row[4]}")
                print(f"Commission           : {row[5]}")
                print(f"Opration status      : {row[6]}")
                print(f"Message              : {row[7]}")
                print(f"Opration Date        : {row[8]}")
                print("=" * 30)

        elif notifiction_det_choice == 3:
            print("search by reference_number for view information of notifiction details: ")
            reference_number = int(input("Enter reference number : "))
            result = Notification_details.search_by_reference_number(db, reference_number )
            if result:
                print("=" * 30)
                print(f"notifiction id       : {result[0]}")
                print(f"reference  number    : {result[1]}")
                print(f"sender_name          : {result[2]}")
                print(f"receiver_name        : {result[3]}")
                print(f"Amount               : {result[4]}")
                print(f"Commission           : {result[5]}")
                print(f"Opration status      : {result[6]}")
                print(f"Message              : {result[7]}")
                print(f"Opration Date        : {result[8]}")
                print("=" * 30)
            else:
                print("No founded with this id")

        elif notifiction_det_choice == 0:
            break

        else:
            print("The number that you chose is wrong !!!")

# --------------------------------------------------
while True:
    print("\n" + "=" * 50)
    print("\tYEMEN CACH\t")
    print("=" * 50)
    print("1- Users Management")
    print("2- Wallets Management")
    print("3- Wallet Currency Management")
    print("4- Currency Management")
    print("5- Transactions Management")
    print("6- Beneficiary Management")
    print("7- Notification Management")
    print("8- Notification_details Management")

    print("=" * 50)

    choice = int(input("Choose Number of Management or 0 for Exit : "))

    if choice == 0:
        print("The Program Closed successfully 🖐")
        break
    elif choice == 1:
        Users_Management(db)

    elif choice == 2:
        Wallets_Management(db)

    elif choice == 3:
        Wallet_Currency_Management(db)

    elif choice == 4:
        Currency_Management(db)

    elif choice == 5:
        Transactions_Management(db)

    elif choice == 6:
        Beneficiary_Management(db)

    elif choice == 7:
        Notification_Management(db)

    elif choice == 8:
        Notification_details_Management(db)

    else:
        print("The number that you chose is wrong !!!")

# --------------------------------------------------
db.close()
# --------------------------------------------------


# objects=[User,Wallet,Wallet_currency,Currency,Transaction
#     ,Beneficiary,Notification,Notification_details]

# for object in objects:
#     print(object.view_all(db))
#     print("-"*40)