
import psycopg2
from config import config


def insert_entries(insert_list):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany("INSERT INTO contacts (name, phone) VALUES(%s, %s)", insert_list)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    contacts = [("denis sharipov", "+77777777777"), ("kostya simple", "87705232243"), ("ilyasperfecto", "88005553535"), ("valeravacovskiy", "87014764323"), ("andreikuharskiy", "87073985407"), ("ilyasmonesko", "87051325323")]
    insert_entries(contacts)