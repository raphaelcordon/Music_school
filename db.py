from constants import bold, red, green, purple
import mysql.connector


msdb = mysql.connector.connect(
    host='localhost',
    user='music_school',
    passwd='Music_school123',
    database='music_school'
)


class ConsultingDB:
    def __init__(self, category):
        cursor = msdb.cursor()
        consulting_query = f"SELECT Name FROM {category}"
        cursor.execute(consulting_query)
        list = cursor.fetchall()
        if not list:
            print(f'   No registries found for {bold(category)} category ')
        else:
            count = 0
            for l in list:
                print(f'[ {purple(l[0])} ] ', end='')
                count += 1
                if count == 5:
                    print()
                    count = 0
            print()


class RegisteringDB:
    def __init__(self, category, new_register):
        if CheckDuplication.check(category, new_register) is True:
            print(red('Already registered in the system'))
        else:
            cursor = msdb.cursor()
            insert = f"INSERT INTO {category} (Name) VALUES (%s)"
            record = new_register
            cursor.execute(insert, (record,))
            msdb.commit()
            print(green(f'   {new_register} successfully registered as a {category}'))


class UpdatingDB:
    def __init__(self, category, item, new_item):
        cursor = msdb.cursor()
        updating_query = f"UPDATE {category} SET name='{new_item}' WHERE name='{item}'"
        cursor.execute(updating_query)
        print(green('Successfully updated.'))


class DeletingDB:
    def __init__(self, category, item):
        cursor = msdb.cursor()
        deleting_query = f"DELETE FROM {category} WHERE name='{item}'"
        cursor.execute(deleting_query)
        print(green('Successfully deleted.'))


class CheckDuplication:
    @staticmethod
    def check(category, item):
        cursor = msdb.cursor()
        consulting_query = f"SELECT * FROM {category} where name = '{item}'"
        cursor.execute(consulting_query)
        list = cursor.fetchall()
        if list:
            return True
