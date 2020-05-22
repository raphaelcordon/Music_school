import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='music_school',
    passwd='Music_school123',
    database='music_school'
)

cursor = mydb.cursor()
#insert = "INSERT INTO courses (coursename) VALUES (%s)"
#record1 = 'Guitar'
#cursor.execute(insert, (record1,))
#mydb.commit()


consulting_query = f"SELECT * FROM course where name = 'Bass'"
cursor.execute(consulting_query)
list = cursor.fetchall()
if not list:
    print('None')
else:
    for l in list:
        print(l[0])


"""
courses_query = "SELECT coursename FROM courses"
cursor.execute(courses_query)
list = cursor.fetchall()
for l in list:
    print(l[0])
print(list)
"""

#my_cursor.execute("CREATE DATABASE testdb")
"""
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    if 'testdb' in my_cursor:
        print('ok')
    else:
        print('não ok')


#my_cursor.execute("CREATE TABLE users (name VARCHAR(100), email VARCHAR(100), age INTEGER(3), user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
#my_cursor.execute("SHOW TABLES")
#for table in my_cursor:
#    print(table[0])

insert = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"

record1 = ('John', "john@john.com", 40)

my_cursor.execute(insert, record1)
mydb.commit()

"""