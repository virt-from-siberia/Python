import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(dbname='testDB', user="postgres", password="postgre", host="localhost", port=5432)
cur = conn.cursor()

# cur.execute("CREATE TABLE test2 (id serial PRIMARY KEY, num integer, data varchar);")
# conn.commit()

# cur.execute("CREATE TABLE super_heroes (hero_id serial PRIMARY KEY, hero_name varchar, strength integer);")
# cur.execute("INSERT INTO super_heroes (hero_name, strength) VALUES(%s, %s)", ('superman', 100))
# cur.execute("""
#             INSERT INTO super_heroes (hero_name, strength)
#             VALUES (%(name)s, %(strength)s)
#             """, {'name': 'green array', 'strength': 80})
# conn.commit()

# cur.execute("CREATE TABLE traffic_light (light_id serial PRIMARY KEY, light text);")
# conn.commit()

# cur.execute("INSERT INTO traffic_light (light) VALUES (%s)", ('red',))
# conn.commit()

# cur.execute("INSERT INTO super_heroes (hero_name, strength) VALUES(%s, %s)", ('flash', 120))
# cur.execute("INSERT INTO super_heroes (hero_name, strength) VALUES(%s, %s)", ('batman', 90))

cur.execute('SELECT * FROM super_heroes')
conn.commit()

one_line = cur.fetchone()
print(one_line)

full_fetch = cur.fetchall()
for record in full_fetch:
    print(record)

cur.close()
conn.close()

with psycopg2.connect(dbname='testDB', user="postgres", password="postgre", host="localhost", port=5432) as conn:
    with conn.cursor(cursor_factory=RealDictCursor) as curs:
        execute_values = (curs, "INSERT INTO traffic_light(light) VALUES %s", [
            ("green",), ("yellow",)
        ])

        curs.execute("SELECT * FROM traffic_light")
        records = curs.fetchall()
        print(records)
