from constants import MAIN_MENU, SUBITEM_MAIN_MENU, bold, red
from db import ConsultingDB, RegisteringDB, UpdatingDB, DeletingDB, CheckDuplication


class BaseSubMenu:
    def __init__(self):
        self.subitem_main_menu = SUBITEM_MAIN_MENU
        for i in range(0, len(self.subitem_main_menu)):
            print(f'   press: {bold(i + 1)} to: {bold(self.subitem_main_menu[i + 1])}')
        option_item = int(input(bold('Choose an option: ')))
        self.option_subitem_main_menu = self.subitem_main_menu[option_item]
        self.choice()

    def choice(self):  # return to class SubMenu in main_menu.py
        from main_menu import MainMenu
        if self.option_subitem_main_menu == MAIN_MENU:
            MainMenu()
        else:
            return self.option_subitem_main_menu


class SubMenuRegister:
    def __init__(self, category):
        self.subitem_main_menu = category
        new_register = str(input(f'Type the new {self.subitem_main_menu} name: ')).strip().title()
        RegisteringDB(self.subitem_main_menu, new_register)


class SubMenuConsultation:
    def __init__(self, category):
        self.subitem_main_menu = category
        print(f'Consult a {self.subitem_main_menu}:')
        ConsultingDB(self.subitem_main_menu)


class SubMenuModification:
    def __init__(self, category):
        self.subitem_main_menu = category
        existing_item = str(input(f'Existing name: ')).strip().title()
        if CheckDuplication.check(self.subitem_main_menu, existing_item) is None:
            print(red('Not found or nonexistent'))
        else:
            new_item = str(input(f'Type the new name: ')).strip().title()
            print(f'Modifying an item from {self.subitem_main_menu}:')
            UpdatingDB(self.subitem_main_menu, existing_item, new_item)


class SubMenuDeleting:
    def __init__(self, category):
        self.subitem_main_menu = category
        deleting_item = str(input(f'Name to be deleted: ')).strip().title()
        print(f'Deleting an item from {self.subitem_main_menu}:')
        DeletingDB(self.subitem_main_menu, deleting_item)