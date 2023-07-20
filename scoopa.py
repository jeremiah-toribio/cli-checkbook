### welcome statement visual as well as menu options associated with user input and its variable ###

print(f'  ___________________________________________________  \n | Welcome to Floppa bank | Access your account here | \n  --------------------------------------------------- \n | Please type 1-4 to select their respective option.| \n |            What would you like to do?             | \n |___________________________________________________|')
print(f'\n [ 1 ] View current balance \n [ 2 ] Record a Debit (Deposit) \n [ 3 ] Record a Credit (Withdrawal) \n [ 4 ] Exit \n   ')


user_input = str(input( '\n' ))

### This is where user input reactions will be initialized ###
#class Transactions:



def user1():
    account_balance = ''
    print(f'Your current balance is: {account_balance}')
    return

def user2():
    return

def user3():
    return

def user4():
    print('Thanks for banking with big floppa')
    return exit()

### Check to see if input is valid and routing to proper functions ###


options = ['1','2','3','4']
#def menu():
#while user_input not in options:

attempts = 3

while attempts != 0:
    if user_input.isdigit() == True:
        if user_input not in options:
            attempts -= 1
            print('Please select only a digit that is an option.')
        elif user_input == '1':
            user1()
        elif user_input == '2':
            user2()
        elif user_input == '3':
            user3()
        elif user_input == '4':
            user4()
        else:
            print('Only numbers.')
    else:
        print('Only digits.')
        attempts -= 1