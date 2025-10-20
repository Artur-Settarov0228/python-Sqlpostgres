import psycopg2

connection = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='02282005',
    database='todo_db'
)
cursor = connection.cursor()

cursor.execute("""
    create table tasks(
        id serial,
        title varchar(128) not null,
        description text,
        due_date date not null,
        create_at date not null 
               
               
    );

""")

connection.commit()
connection.close()