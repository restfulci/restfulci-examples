import psycopg2

conn = psycopg2.connect("host='postgres' port='5432' dbname='foo' user='postgres' password='postgres'")
cur = conn.cursor()
cur.execute("""SELECT datname from pg_database""")
records = cur.fetchall()

print(records)
