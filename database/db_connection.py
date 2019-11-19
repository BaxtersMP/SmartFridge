import sqlite3


class DBNames:
    db = r'C:\Users\befor\PyProjects\SmartFridge\db\Lexicon.db'


def db_connect():
    return sqlite3.connect(DBNames.db)


# db = db_connect()
#
#
# def get_perishable_lifespan(db_name, persihable_type):
#     sql = """select * from perishable_type"""
#     cursor = db_name.cursor()
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)
#
#
# get_perishable_lifespan(db, 'food')
