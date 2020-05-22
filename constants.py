MAIN_MENU = 'Main Menu'

ITEM_MAIN_MENU = {1: 'New Register', 2: 'Consult', 3: 'Modify', 4: 'Delete', 5: 'Quit'}
SUBITEM_MAIN_MENU = {1: 'Course', 2: 'Instructor', 3: 'Student', 4: 'Main Menu'}
HEAD_SUB_MENU = {1: 'Registration area', 2:'Consultation area'}

# Sub Menu Items
NEW_REGISTER = 'New Register'
CONSULT = 'Consult'
MODIFY = 'Modify'
DELETE = 'Delete'

####################################
# functions to change color schema:#
####################################


def grey(head):  # Grey background with black letters
    return(f'   \033[1:47m{head}\033[m')


def bold(head):  # Bold Letters
    return(f'\033[1m{head}\033[m')


def red(head):  # Bold and red Letters
    return(f'\033[1:31m{head}\033[m')


def green(head):  # Bold Black letter and green Background
    return(f'\033[1:42m{head}\033[m')


def purple(head): # Bold Purple letter
    return (f'\033[1:35m{head}\033[m')

####################################
