import psycopg2

def get_perishable_lifespan(persihable_type):
    sql = """SELECT lifespan
        FROM perishable_type
        WHERE type = %s"""
    cursor.execute(sql, persihable_type)
