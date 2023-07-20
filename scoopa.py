### welcome statement visual as well as menu options associated with user input and its variable ###

print(f'  ___________________________________________________  \n | Welcome to Floppa bank | Access your account here | \n  --------------------------------------------------- \n | Please type 1-4 to select their respective option.| \n |            What would you like to do?             | \n |___________________________________________________|')
print(f'\n [ a ] View current balance \n [ b ] Record a Debit (Deposit) \n [ c ] Record a Credit (Withdrawal) \n [ d ] Exit \n   \n')


### This is where user input reactions will be initialized ###
#class Transactions:


def user2():
    return

def user3():
    return

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

### Check to see if input is valid and routing to proper functions ###


options = ['a','b','c','d']
account_balance = ''


attempts = 3
while attempts != 0:
    user_input = str(input())
    if user_input not in options:
        attempts -= 1
        print(f'Please select only a letter that is an option. \nYou have {attempts} attempt left before you are removed.')
    elif user_input == 'a':
        print(f'Your current balance is: {account_balance}')

        break
    elif user_input == 'b':
        print(f'How much would you like to deposit today? We are not accepting change.')
        deposit = int(input())
        break
    elif user_input == 'c':
        user3()
        break
    elif user_input == 'd':
        exiter()
    else:
        print(f'Please select only a letter that is an option. \nYou have {attempts} attempt left before you are removed.')
        attempts -= 1
