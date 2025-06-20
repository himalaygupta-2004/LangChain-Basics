import sqlite3
# Create database 
connection = sqlite3.connect("student.db")

# create cursor
cursor = connection.cursor()

# create table
create_table_query = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    COURSE VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);"""
cursor.execute(create_table_query)

# insert Records
insert_query = """INSERT INTO STUDENT(NAME,COURSE,SECTION,MARKS) VALUES (?,?,?,?)"""
values = [('Rahul', 'Btech', 'CSE', 90),
('Rahul', 'Btech', 'CSE', 90),
('Raj', 'Btech', 'AI/ML', 80),
('Krish', 'Btech', 'CSE', 70),
('Kapil', 'Btech', 'AI/ML', 60)]

cursor.executemany(insert_query,values)
connection.commit()

data = cursor.execute("""SELECT * FROM STUDENT""")

for row in data:
    print(row)

if(connection):
    connection.close()