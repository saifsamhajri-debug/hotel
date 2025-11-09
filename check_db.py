import sqlite3
import os

# Check which database file exists
db_paths = ['instance/hotel.db', 'hotel.db']
for db_path in db_paths:
    if os.path.exists(db_path):
        print(f"Using database: {db_path}")
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # Drop temporary table if it exists
        cur.execute("DROP TABLE IF EXISTS _alembic_tmp_customers")
        conn.commit()
        print("Dropped temporary table if it existed")

        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cur.fetchall()
        print('Tables:', tables)

        if ('customers',) in tables:
            cur.execute("PRAGMA table_info(customers)")
            columns = cur.fetchall()
            print('Customer columns:', columns)

        if ('alembic_version',) in tables:
            cur.execute("SELECT * FROM alembic_version")
            version = cur.fetchall()
            print('Alembic version:', version)

        conn.close()
        break
else:
    print("No database file found")