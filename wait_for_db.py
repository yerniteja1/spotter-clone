import time
import psycopg2
import os

def wait():
    print("Waiting for database...")
    while True:
        try:
            conn = psycopg2.connect(
                dbname=os.getenv('DB_NAME'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST', 'localhost'),
                port=os.getenv('DB_PORT', '5432'),
            )
            conn.close()
            print("Database ready.")
            break
        except psycopg2.OperationalError:
            print("Not ready yet — retrying in 1s...")
            time.sleep(1)

wait()