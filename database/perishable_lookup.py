from database.db_connection import db_connect

db = db_connect()


def get_perishable_lifespan(db_name, persihable_type):
    sql = """select * from perishable_type where name = ?"""
    cursor = db_name.cursor()
    cursor.execute(sql, (persihable_type,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)


get_perishable_lifespan(db, 'fruit')
