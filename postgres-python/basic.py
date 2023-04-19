import psycopg2
def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="2424", host="localhost", port="5433")
    print('Connected Successfully')
    cursor = conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print('Table created successfully')
    conn.commit()
    conn.close()

def insert():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="2424", host="localhost", port="5433")
    print('Connected Successfully')
    cursor = conn.cursor()
    cursor.execute('''insert into employees(Name, ID, Age) values ('Sam', 011, 34);''')
    print('Data inserted successfullly')
    conn.commit()
    conn.close()

def extract():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="2424", host="localhost", port="5433")
    print('Connected Successfully')
    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    # print(cursor.fetchone())
    show = cursor.fetchone()
    print(show)
    # print('Data inserted successfullly')
    conn.commit()
    conn.close()

def insertValuesFromUser():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="2424", host="localhost", port="5433")
    print('Connected Successfully')
    cursor = conn.cursor()
    name = input('Enter a name')
    id = input('Enter a id')
    age = input('Enter a age')
    query = '''insert into employees(Name, ID, Age) values (%s, %s, %s);'''
    cursor.execute(query, (name, id, age))
    print('Data inserted successfullly')
    conn.commit()
    conn.close()
insertValuesFromUser()