import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_all_rows(query):
    try:
        conn = psycopg2.connect(
            host=os.getenv("PG_HOST"),
            port=5432,
            database=os.getenv("PG_DBNAME"),
            user=os.getenv("PG_UNAME"),
            password=os.getenv("PG_PASSWD"),
        )
        # Create a cursor
        cur = conn.cursor()
        # Execute the query to get row count
        cur.execute(query)
        # Fetch the result
        rows = cur.fetchall()
        # Close the cursor and connection
        cur.close()
        conn.close()
        # Print the row count
        return True, rows

    except (Exception, psycopg2.DatabaseError) as error:
        if cur:
            cur.close()
        if conn:
            conn.close()
        return False, error


def get_one_row(query):
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="swym",
            user="swymdev",
            password="swym",
        )
        # Create a cursor
        cur = conn.cursor()
        # Execute the query to get row count
        cur.execute(query)
        # Fetch the result
        rows = cur.fetchone()
        # Close the cursor and connection
        cur.close()
        conn.close()
        # Print the row count
        return True, rows

    except (Exception, psycopg2.DatabaseError) as error:
        if cur:
            cur.close()
        if conn:
            conn.close()
        return False, error
