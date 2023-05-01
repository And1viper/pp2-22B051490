import psycopg2
from config import config
import csv

def create_list_from_cvs(path):
    the_list = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader) 
        for row in reader:
            name, phone = row
            the_list.append((name, phone))
    return the_list

def upload_row_cvs():
    path = input("Enter the path: ")
    sql_query = """INSERT INTO contacts(name, phone)
             VALUES(%s, %s) RETURNING id;"""
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        #add row 
        cur.executemany(sql_query, create_list_from_cvs(path))
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def upload_row():
    name = input("Write name: ")
    phone = input("Write phone: ")
    sql_query = """INSERT INTO contacts(name, phone)
             VALUES(%s, %s) RETURNING id;"""
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        #add row 
        cur.execute(sql_query, (name, phone))
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def update_row():
    opt = input("What do you want to update, name or phone? ")
    new_val = input("Updated value: ")
    id = input("Id of the row: ")
    sql_query = """UPDATE contacts
                SET """+ opt +""" = %s
                WHERE id = %s"""
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        #add row 
        cur.execute(sql_query, (new_val, id))
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def query_data():
    filters = []
    while True:
        col = input("Write the column_name by which it will be filtered. Wrtie 'done' when done: ")
        if col == "done":
            break
        val = input("Write the value by which it will be filtered: ")
        filters.append((col, val))
    sql_query = "SELECT * FROM contacts"
    if len(filters) != 0:
        sql_query += " WHERE "
        for filter in filters:
            sql_query += filter[0] + " LIKE '%" + filter[1] + "%' AND "
    sql_query = sql_query[:len(sql_query)-4]
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        #filtered
        cur.execute(sql_query)
        rows = cur.fetchall()
        print("The number of parts:", cur.rowcount)
        for row in rows:
            print(row)
        # close communication with the PostgreSQL database server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def delete_rows():
    opt = input("By which column you want to delete, name or phone? ")
    del_val = input("Enter the value by which entries should be deleted: ")
    sql_query = """DELETE FROM contacts
                WHERE """+ opt +""" = %s"""
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        #add row 
        cur.execute(sql_query, (del_val,))
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    while True:
        opt = input("Choose the option:\n(1) - upload csv file\n(2) - enter the name and phone to upload it\n(3) - update row\n(4) - query data\n(5) - delete row\n")
        if int(opt) == 1:
            upload_row_cvs()
            break
        elif int(opt)== 2:
            upload_row()
            break
        elif int(opt) == 3:
            update_row()
            break
        elif int(opt) == 4:
            query_data()
            break
        elif int(opt) == 5:
            delete_rows()
            break
        else:
            print("Invalid option")