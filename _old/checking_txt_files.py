"""
import main_menu

# Pack of def for checking files:


def readfile(filename):  # Read a file and print what's in there.
    try:
        a = open(filename, 'rt')
    except:
        print(f"File couldn't be ready")
    else:
        return f'\033[1:34m{a.read()}\033[m'


def appending(filename, info):  # Append a new item in a file.
    try:
        a = open(filename, 'at')
    except:
        raise FileNotFoundError
    else:
        a.write(f'{info}\n')
        a.close()


def checkduplication(filename, info):
    # Check for duplications in a file and break to the menu if info is existent.
    with open(filename, 'rt') as a:
        if info in a.read():
            print(f'\033[1:31mAlready registered in the system\033[m')
            a.close()
            main_menu.SubMenu(1)
        else:
            confirm = ''
            while True:
                confirm = str(input(f'Confirm registering "\033[1m{info}\033[m"? [Y/N]')).strip().lower()
                if confirm == 'y' or confirm == 'n':
                    break
            if confirm == 'y':
                appending(filename, info)
                print('\033[1mSuccessfully registered\033[m')
                main_menu.SubMenu(1)
            elif confirm == 'n':
                main_menu.SubMenu(1)
"""