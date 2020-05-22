from sub_menus_base import BaseSubMenu, SubMenuRegister, SubMenuConsultation, SubMenuModification, SubMenuDeleting
from constants import ITEM_MAIN_MENU, NEW_REGISTER, CONSULT, MODIFY, DELETE, grey, bold


class MainMenu:
    def __init__(self):
        self.item = ITEM_MAIN_MENU
        print('Possible actions:')
        for i, v in self.item.items():
            print(f'   Press {bold(i)} to: {bold(v)}')

        while True:
            option = int(input(bold('Choose an action: ')))
            if option in ITEM_MAIN_MENU:
                self.option_main_menu = self.item[option]
                if self.option_main_menu == 'Quit':
                    print(bold('  -- Closing application --'))
                    quit()
                else:
                    while True:
                        SubMenu(self.option_main_menu)


class SubMenu():
    def __init__(self, option_main_menu):
        choice_sub_menu = BaseSubMenu().choice()
        self.option_main_menu = option_main_menu
        self.choice_sub_menu = choice_sub_menu
        if self.option_main_menu == NEW_REGISTER:
            print(grey('Registration area'))
            SubMenuRegister(self.choice_sub_menu)
        elif self.option_main_menu == CONSULT:
            print(grey('Consultation area'))
            SubMenuConsultation(self.choice_sub_menu)
        elif self.option_main_menu == MODIFY:
            print(grey('Modification area'))
            SubMenuModification(self.choice_sub_menu)
        elif self.option_main_menu == DELETE:
            print(grey('Deleting area'))
            SubMenuDeleting(self.choice_sub_menu)
