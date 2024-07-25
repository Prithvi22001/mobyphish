import psycopg2

# Database connection parameters
DB_NAME = 'moby'
DB_USER = 'admin'
DB_PASSWORD = 'moby'
DB_HOST = '137.99.25.227'
DB_PORT = '5432'
user_notcompleted=[]
user_completed=[]
study_completed=[]
time_task={}
avg_time=[]

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def check_time_taken(conn):

    with conn.cursor() as cursor:
        query = """
        SELECT i.id,u.user_id,(i. time_end - i.time_start) AS time_taken
        FROM myapp_item i
        JOIN myapp_user u ON i.user_id=u.id
        WHERE i.time_start IS NOT NULL AND i.time_end IS NOT NULL;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            user_id=row[1]
            time_taken=row[2]
            if user_id not in time_task:
                time_task[user_id]=[]
            time_task[user_id].append(time_taken)
            avg_time.append(time_taken)

            # print(f"Item ID: {row[0]},User ID: {row[1]} ,Time Taken: {row[2]}")

        query = """
        SELECT i.id,u.user_id,(i. time_end - i.time_start) AS time_taken
        FROM myapp_itemdump i
        JOIN myapp_user u ON i.user_id=u.id
        WHERE i.time_start IS NOT NULL AND i.time_end IS NOT NULL;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            user_id=row[1]
            time_taken=row[2]
            if user_id not in time_task:
                time_task[user_id]=[]
            time_task[user_id].append(time_taken)
            avg_time.append(time_taken)

            # print(f"ROUND 1 Item ID: {row[0]},User ID: {row[1]} ,Time Taken: {row[2]}")

        for k in time_task:
            if k in user_notcompleted:
                pass
            else:
                study_completed.append(time_task[k])

def check_time_taken_bank(conn):
    avg_time_bank=[]
    with conn.cursor() as cursor:
        query = """
        SELECT i.id,u.user_id,(i. time_end - i.bank_vist) AS time_taken
        FROM myapp_item i
        JOIN myapp_user u ON i.user_id=u.id
        WHERE i.time_start IS NOT NULL AND i.time_end IS NOT NULL;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            user_id=row[1]
            time_taken=row[2]
            avg_time_bank.append(time_taken)

            # print(f"Item ID: {row[0]},User ID: {row[1]} ,Time Taken: {row[2]}")

        query = """
        SELECT i.id,u.user_id,(i. time_end - i.bank_vist) AS time_taken
        FROM myapp_itemdump i
        JOIN myapp_user u ON i.user_id=u.id
        WHERE i.time_start IS NOT NULL AND i.time_end IS NOT NULL;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            user_id=row[1]
            time_taken=row[2]
            avg_time_bank.append(time_taken)

            # print(f"ROUND 1 Item ID: {row[0]},User ID: {row[1]} ,Time Taken: {row[2]}")

        # for k in time_task:
        #     if k in user_notcompleted:
        #         pass
        #     else:
        #         study_completed.append(time_task[k])
            
        # print(f"--AVG BANK:{avg_time_bank}")
        return sum(avg_time_bank)/len(avg_time_bank)




def check_default_status(conn):
    global user_completed
    with conn.cursor() as cursor:
        query = """
        SELECT u.user_id
        FROM myapp_user u
        JOIN myapp_item i ON u.id = i.user_id
        WHERE i.status = 'default';
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            user_notcompleted.append(row[0])
            # print(f"User ID: {row[0]} has an item with 'default' status")
        
        query = """
        SELECT u.user_id
        FROM myapp_user u
        JOIN myapp_itemdump i ON u.id = i.user_id
        WHERE i.status = 'default';
        """
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            user_notcompleted.append(row[0])
            # print(f"User ID: {row[0]} has an item with 'default' status in round 1")

        # Get all user_ids that exist in both Item and ItemDump tables
        cursor.execute("""
            SELECT DISTINCT u.user_id
            FROM myapp_user u
            WHERE EXISTS (
                SELECT 1
                FROM myapp_item i
                WHERE i.user_id = u.id
            )
            AND EXISTS (
                SELECT 1
                FROM myapp_itemdump id
                WHERE id.user_id = u.id
            );
        """)
        users_in_both_tables = set(row[0] for row in cursor.fetchall())

        # Filter users without 'default' status in both tables
        users_without_default = users_in_both_tables - set(user_notcompleted)
        user_completed=users_without_default
        # print(users_without_default)

# def get_times_for_user(conn,user_id):
#     with conn.cursor() as cursor:
#         # First time in ItemDump for the user
#         cursor.execute('''
#             SELECT MIN(time_start) 
#             FROM myapp_itemdump 
#             WHERE user_id = %s AND status != 'default'
#         ''', [user_id])
#         first_time_itemdump = cursor.fetchone()[0]

#         # Last time in Item for the user
#         cursor.execute('''
#             SELECT MAX(time_end) 
#             FROM myapp_item 
#             WHERE user_id = %s AND status != 'default'
#         ''', [user_id])
#         last_time_item = cursor.fetchone()[0]

#     return first_time_itemdump, last_time_item

# # Example usage:
# user_id = 'some_user_id'  # Replace with the actual user ID
# first_time, last_time = get_times_for_user(user_id)
# print(f"First time in ItemDump: {first_time}")
# print(f"Last time in Item: {last_time}")


def main():
    conn = connect_to_db()
    avg_allround=[]
    if conn:
        check_default_status(conn)
        check_time_taken(conn)
        print(f"AVG TIME SPENT ON BANK PAGE: {check_time_taken_bank(conn)}")
        time_per_study=0
        # for users in user_completed:
        #     s,e=get_times_for_user(conn,users)
        #     avg_allround.append(e-s)
        both_rounds=0
        # print(f"----TOTAL TIME FOR BOTH ROUNDS---{sum(avg_allround)/len(avg_allround    )}")
        # print(time_task)
        for i in study_completed:
            if len(i)>=10:
                both_rounds+=1
                time_per_study+=sum(i)
        avg_time_per_study=time_per_study/both_rounds
        print(f"AVG TIME PER TASK:{sum(avg_time)/len(avg_time)} \nUsers who did not complete the study: {len(set(user_notcompleted))} \n")
#  Avg time taken to complete all tasks :{avg_time_per_study}
        conn.close()



if __name__ == '__main__':
    main()
