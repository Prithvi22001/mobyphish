import psycopg2
from psycopg2 import sql
from mail import send_mail
# Database connection parameters
DB_HOST = '137.99.25.227'
DB_NAME = 'moby'
DB_USER = 'admin'
DB_PASSWORD = 'moby'
DB_PORT = '5432'  # Default is '5432'

def delete_all_blocked_users():
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        
        # Create a cursor object
        cur = conn.cursor()

        # Define the SQL query to delete all records from BlockedUser table
        query = sql.SQL("DELETE FROM {table}").format(
            table=sql.Identifier('myapp_blockeduser')  # Replace with your table name if different
        )

        # Execute the query
        cur.execute(query)

        # Get the number of rows deleted
        rows_deleted = cur.rowcount

        # Commit the transaction
        conn.commit()

        # Print the number of deleted rows
        print(f"{rows_deleted} record(s) deleted from BlockedUser table.")
        send_mail('Weekly Statistics',f'Number of user completed last weeks tasks :{rows_deleted}',['prithvi.shah@uconn.edu'])
        # Close the cursor and connection
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

# Run the function to delete all records
delete_all_blocked_users()
