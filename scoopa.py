# importing necessary libraries csv for data dump and time for logging

import csv
import time

# initializes csv file
columns = ['time','type','amount']
with open('account.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames = columns)
        

# return to menu function
def return_menu():
    print('\nWould you like to return to menu?\n Please enter: (y/n)')
    return_options = ['y','n']
    return_attempts = 3
    while return_attempts != 0:
        menu1 = str(input())
        #if return_attempts == 0:
            #exiter()
        if menu1.lower() == 'y':
            return main_menu()
        elif menu1.lower() == 'n':
            exiter()
        elif return_attempts == 0:
            exit()
        else:
            print(f'Please type only y or n.\nYou have {return_attempts} attempt left before you are removed.')
            return_attempts -= 1

    return

### original starting menu with displays
def main_menu():
    ### welcome statement visual as well as menu options associated with user input and its variable ###
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣦⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⠟⠁⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⡄⢻⣿⡇⠀⠀⠀⠀⠀⠀⢸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣿⣿⠟⠁⠀⢀⡼
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⢾⣧⣤⢿⡧⠀⠀⠀⠰⣤⡀⢈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡿⢟⣵⣿⡟⠁⠀⠀⣴⠋⠀
⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣨⣤⣤⠿⠆⠀⠀⠀⠀⠀⠉⠛⠾⣧⣤⣀⣀⡀⠀⠀⢀⣠⣶⣿⣿⡟⢉⣴⣿⡿⠁⠀⠀⣠⠞⠁⠀⠀
⣿⠇⠀⠀⠀⠀⠀⣀⣴⡿⠿⠋⠀⠀⠀⠀⠀⢀⣀⡀⣶⠂⠀⠀⠀⠻⣯⣭⡛⠶⣶⣿⣿⣿⣏⣡⣴⣿⡟⠉⠀⠀⢀⡼⠃⠀⠀⠀⠀
⠏⠀⠀⠀⣀⣴⡾⠟⠛⠁⠀⠀⠀⠀⠀⠀⠚⢻⣿⣵⣏⠀⠀⠀⠀⠀⠘⢿⣇⠀⠀⠈⠻⢮⡛⣿⣿⠏⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀
⠁⣀⠀⣾⠟⠋⠀⠀⠀⠀⣠⣾⣶⣤⣀⡀⢀⠈⠻⣿⣿⣹⡄⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠈⢷⡌⠻⣦⠀⠀⠶⠟⠀⠀⠀⠀⠀⠀⠀
⢠⣿⠟⠁⠀⠀⠀⢀⣼⣿⣿⡟⠉⠉⠉⠋⠈⠁⠒⣿⣿⣿⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠈⣿⣧⠈⢷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢿⣿⠄⠀⠠⠄⠴⣾⣿⣿⣥⣤⣤⣾⣿⣿⣟⣳⣀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣧⠃⠀⠀⠀⣿⣿⡟⠀⣹⣦⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡇⠀⠀⠀⠀⢺⣿⡟⢿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣆⠀⠀⢄⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀⢿⣿⠟⠈⠟⠻⢷⡀⠀⠀⠀⠀⠀⠀
⢿⣷⢠⣶⠆⠀⢸⢯⣤⠀⠛⢿⣿⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⠈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣴⣦⣤⣤⡈⣻⡀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣶⠇⠈⠈⠹⠧⣄⡀⠙⠲⢿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣯⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀
⣾⣿⣿⣿⣷⣦⠉⠀⠀⠀⠈⠉⠑⠂⠀⠈⠙⢿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠼⠂⠀⠀⠀⣿⣿⣿⣿⣿⣿⡟⠀⣿⣇⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⠈⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⣠⣼⣄⠀⠀⢸⣿⣮⣿⣿⠿⠋⠀⣰⣉⢸⡆⠀⠀⠀
⠀⠀⠙⣿⣿⣿⣿⣷⣦⠀⣤⡀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠉⠀⠈⠁⠁⣸⣿⣿⠇⠀⠠⠾⠛⠋⠀⠈⣿⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣿⣿⣿⣶⣸⣷⠀⠀⠀⠀⠀⠀⠀⢸⡿⣿⣿⣿⡆⠀⣦⡀⠀⠀⠀⠀⠀⠀⢹⣿⣧⣀⠀⠀⠀⠀⠀⠀⢀⣻⣆⠀⠀
⠀⠀⠀⠀⠘⠿⠿⣿⣿⣿⣿⣿⣿⡶⢶⡿⠥⡄⠀⠀⠁⠙⣿⣿⣿⣆⣿⣿⣶⣤⣤⣀⣠⡄⠈⣿⣿⣇⠁⠀⠀⠀⠀⠀⠈⠉⢻⡄⠀
⠂⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣿⣿⣷⣿⣶⣄⣠⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠁⠀⠉⠙⢿⡹⣿⣿⡏⠹⠆⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿⣿⣿⣄⡄⠀⠀⠀⠘⣿⣿⣿⣿⣧⠀⢰⠀⠈⣷⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣁⡀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⢀⣾⡇⣾⣿⠿⠁⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠚⣿⠀⠀⠀⠀⠀⠀⠀⢠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣧⣤⣄⠀⠀⠀⠀⠀⠀⠘⣿⣿⡿⠋⠀⠀⠀⠀⠀⣀⣤⣴⣿⠀⠀⠀⠀⠀⠀⠀⢸
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⠿⠶⣶⣶⣶⠶⢀⣼⣿⡁⠰⣤⣄⡀⠀⠀⣈⣹⡿⠁⠀⣀⣠⣤⣀⣤⣤⣿
⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢿⣿⡿⠟⠛⠻⠿⠛⠛⠋⠙⠻⢶⣬⣭⣍⣭⡿⠛⣉⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣇⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣄⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢫⣟⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿
⣿⣿⣿⣿⣿⣇⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀
          ''')
    print(f'  ___________________________________________________  \n | Welcome to Floppa bank | Access your account here | \n  --------------------------------------------------- \n | Please type 1-4 to select their respective option.| \n |            What would you like to do?             | \n |___________________________________________________|')
    print(f'\n [ a ] View current balance \n [ b ] Record a Debit (Deposit) \n [ c ] Record a Credit (Withdrawal) \n [ d ] Exit \n')
    
    ### check for user input matches
    options = ['a','b','c','d']

    ### removing from program if unsuccessful attempts exceed 3
    attempts = 3
    while attempts != 0:
        user_input = str(input())
        if user_input.lower() not in options:
            attempts -= 1
            print(f'Please select only a letter that is an option. \nYou have {attempts} attempt left before you are removed.')
        elif user_input.lower() == 'a':
            user1()
            continue
        elif user_input.lower() == 'b':
            user2()
            continue
        elif user_input.lower() == 'c':
            user3()
            break
        elif user_input.lower() == 'd':
            exiter()
        else:
            print(f'Please select only a letter that is an option. \nYou have {attempts} attempt left before you are removed.')
            attempts -= 1

    return


### deposit function
def user2():
    print(f'\nHow much would you like to deposit today? Exact amounts only.')
    global account_balance
    attempts2 = 3
    deposit = 0
    new_balance_deb = 0
    transaction_deb = {}

    #filter for input
    while attempts2 != 0:
        user_input2 = input()
        if user_input2.isdigit() == True:
            deposit = int(user_input2)
            break
        else:
            print(f'Please input only whole numbers.\nYou have {attempts2} attempt left before you are removed.')
            attempts2 -= 1
    

    # needs to call on account balance and save values as input.
    new_balance_deb = deposit + account_balance
    print(f'{new_balance_deb} is your new total balance.')
    # how deposits will be formated into account.csv (ledger)
    transaction_deb = {f'time':time.ctime(),
                        'type':'Debit', 'amount':(deposit)}
                        #'balance':(new_balance_deb)}
                        
    # actual push of transaction to ledger
    with open('account.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames = columns)
        #writer.writeheader()
        writer.writerow(transaction_deb)
    
    account_balance = new_balance_deb
    return_menu()
    return 

# withdrawal function
def user3():
    print(f'\nHow much would you like to withdrawal today? Exact amounts only.')
    global account_balance
    attempts3 = 3
    withdrawal = 0
    new_balance_cred = 0
    transaction_cred = {}

    # filter for input
    while attempts3 != 0:
        user_input3 = input()
        if user_input3.isdigit() == True:
            withdrawal = int(user_input3) * -1
            break
        else:
            print(f'Please input only whole numbers.\nYou have {attempts3} attempt left before you are removed.')
            attempts3 -= 1
    
    # needs to call on account balance and save values as input.
    new_balance_cred = account_balance + withdrawal
    print(f'{new_balance_cred} is your new total balance.')

    # how withdrawals will be formated into account.csv (ledger)
    transaction_cred = {f'time':time.ctime(),
                        'type':'Credit', 'amount':(withdrawal)}
                        
    # actual push of transaction to ledger
    with open('account.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames = columns)
        #writer.writeheader()
        writer.writerow(transaction_cred)
    

    account_balance = new_balance_cred
    return_menu()
    return

# account balance check
def user1():
    print(f'\nYour current balance is: {account_balance}')
    return_menu()
    return

#ASCII art and exit function
def exiter():
    print('''
          Thank you for banking with big floppa\n
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣿⣿⣦⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⠟⠁⢀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⡄⢻⣿⡇⠀⠀⠀⠀⠀⠀⢸⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣿⣿⠟⠁⠀⢀⡼
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⢾⣧⣤⢿⡧⠀⠀⠀⠰⣤⡀⢈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⡿⢟⣵⣿⡟⠁⠀⠀⣴⠋⠀
⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣨⣤⣤⠿⠆⠀⠀⠀⠀⠀⠉⠛⠾⣧⣤⣀⣀⡀⠀⠀⢀⣠⣶⣿⣿⡟⢉⣴⣿⡿⠁⠀⠀⣠⠞⠁⠀⠀
⣿⠇⠀⠀⠀⠀⠀⣀⣴⡿⠿⠋⠀⠀⠀⠀⠀⢀⣀⡀⣶⠂⠀⠀⠀⠻⣯⣭⡛⠶⣶⣿⣿⣿⣏⣡⣴⣿⡟⠉⠀⠀⢀⡼⠃⠀⠀⠀⠀
⠏⠀⠀⠀⣀⣴⡾⠟⠛⠁⠀⠀⠀⠀⠀⠀⠚⢻⣿⣵⣏⠀⠀⠀⠀⠀⠘⢿⣇⠀⠀⠈⠻⢮⡛⣿⣿⠏⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀
⠁⣀⠀⣾⠟⠋⠀⠀⠀⠀⣠⣾⣶⣤⣀⡀⢀⠈⠻⣿⣿⣹⡄⠀⠀⠀⠀⠘⣿⡀⠀⠀⠀⠈⢷⡌⠻⣦⠀⠀⠶⠟⠀⠀⠀⠀⠀⠀⠀
⢠⣿⠟⠁⠀⠀⠀⢀⣼⣿⣿⡟⠉⠉⠉⠋⠈⠁⠒⣿⣿⣿⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠈⣿⣧⠈⢷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢿⣿⠄⠀⠠⠄⠴⣾⣿⣿⣥⣤⣤⣾⣿⣿⣟⣳⣀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣧⠃⠀⠀⠀⣿⣿⡟⠀⣹⣦⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡇⠀⠀⠀⠀⢺⣿⡟⢿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣆⠀⠀⢄⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀⢿⣿⠟⠈⠟⠻⢷⡀⠀⠀⠀⠀⠀⠀
⢿⣷⢠⣶⠆⠀⢸⢯⣤⠀⠛⢿⣿⣾⣿⣿⣿⣿⣿⣿⣿⡄⠀⠈⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣴⣦⣤⣤⡈⣻⡀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣶⠇⠈⠈⠹⠧⣄⡀⠙⠲⢿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣯⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀
⣾⣿⣿⣿⣷⣦⠉⠀⠀⠀⠈⠉⠑⠂⠀⠈⠙⢿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠼⠂⠀⠀⠀⣿⣿⣿⣿⣿⣿⡟⠀⣿⣇⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣇⠈⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⣠⣼⣄⠀⠀⢸⣿⣮⣿⣿⠿⠋⠀⣰⣉⢸⡆⠀⠀⠀
⠀⠀⠙⣿⣿⣿⣿⣷⣦⠀⣤⡀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠉⠀⠈⠁⠁⣸⣿⣿⠇⠀⠠⠾⠛⠋⠀⠈⣿⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣿⣿⣿⣶⣸⣷⠀⠀⠀⠀⠀⠀⠀⢸⡿⣿⣿⣿⡆⠀⣦⡀⠀⠀⠀⠀⠀⠀⢹⣿⣧⣀⠀⠀⠀⠀⠀⠀⢀⣻⣆⠀⠀
⠀⠀⠀⠀⠘⠿⠿⣿⣿⣿⣿⣿⣿⡶⢶⡿⠥⡄⠀⠀⠁⠙⣿⣿⣿⣆⣿⣿⣶⣤⣤⣀⣠⡄⠈⣿⣿⣇⠁⠀⠀⠀⠀⠀⠈⠉⢻⡄⠀
⠂⠀⠀⠀⠀⠀⠀⠀⠈⠉⢿⣿⣿⣷⣿⣶⣄⣠⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠁⠀⠉⠙⢿⡹⣿⣿⡏⠹⠆⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿⣿⣿⣄⡄⠀⠀⠀⠘⣿⣿⣿⣿⣧⠀⢰⠀⠈⣷⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣁⡀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⢀⣾⡇⣾⣿⠿⠁⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠚⣿⠀⠀⠀⠀⠀⠀⠀⢠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣧⣤⣄⠀⠀⠀⠀⠀⠀⠘⣿⣿⡿⠋⠀⠀⠀⠀⠀⣀⣤⣴⣿⠀⠀⠀⠀⠀⠀⠀⢸
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⠿⠶⣶⣶⣶⠶⢀⣼⣿⡁⠰⣤⣄⡀⠀⠀⣈⣹⡿⠁⠀⣀⣠⣤⣀⣤⣤⣿
⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⢿⣿⡿⠟⠛⠻⠿⠛⠛⠋⠙⠻⢶⣬⣭⣍⣭⡿⠛⣉⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣇⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣄⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢫⣟⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿
⣿⣿⣿⣿⣿⣇⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀
          ''')
    return exit()

# convert input to int
def balance_cvt(num):
    return int(num)

#format of csv file
columns = ['time','type','amount']

#reading of csv file to extract existing rows
with open('account.csv', 'r') as f:
    content = csv.DictReader(f, fieldnames=columns)
    lines = []
    for line in content:
        lines.append(line)

#getting total account balance from iterating transactions
account_balance = 0
for line in lines:
    account_balance = account_balance + balance_cvt(line['amount'])


main_menu()

