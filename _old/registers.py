"""
from checking_txt_files import *
from db import ConsultingDB
from constants import TXT_COURSE, TXT_INSTRUCTOR, TXT_STUDENT


class GeneralRegistering:

    def __init__(self, category, input, menu_position):
        self.category = category
        self.input = input

        ConsultingDB(self.category)

        with open(self.category, 'r') as a:  # If the file is empty, the item if added without further verification.
            a.seek(0)
            first_char = a.read(1)

            if not first_char:
                print(f'"\033[1m{self.input}\033[m" is the first registry')
                appending(self.category, self.input)
                BackSubMenu(menu_position)

            else:  # Show the courses registered, append new ones or break to the menu if duplicated.
                print('\033[1mBefore registering\033[m')
                print('   Please check what is already registered in the system:')
                ListingFileContent(a)
                print()
                checkduplication(self.category, self.input)


class Courses:

    def __init__(self, new_course, menu_position):
        self.course = new_course
        GeneralRegistering(TXT_COURSE, self.course, menu_position)
        BackSubMenu(menu_position)


class Instructors:

    def __init__(self, new_instructor, menu_position):
        self.instructor = new_instructor
        GeneralRegistering(TXT_INSTRUCTOR, self.instructor, menu_position)
        BackSubMenu(menu_position)


class Students:

    def __init__(self, new_student, menu_position):
        self.student = new_student
        GeneralRegistering(TXT_STUDENT, self.student, menu_position)
        BackSubMenu(menu_position)


class BackSubMenu:

    def __init__(self, menu_position):
        from sub_menus_base import SubMenuRegister
        SubMenuRegister(menu_position)


class ListingFileContent:

    def __init__(self, file):
        self.file = file
        try:
            self.listing()
        except:
            self.file = open(file, 'r')
            self.listing()
            self.file.close()

    def listing(self):
        self.file.seek(0)
        lines = list(self.file)
        count = 0
        for r in lines:
            print(f'[ \033[1;35m{r.strip()}\033[m ] ', end='')
            count += 1
            if count == 5:
                print()
                count = 0
        print()
"""