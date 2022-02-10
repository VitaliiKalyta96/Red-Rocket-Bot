import mysql.connector


def connect(database_file):
    connection_db = mysql.connector.connect(
        host="db",
        user="user",
        passwd="user",
        port="3306",
        database=database_file
    )
    if connection_db.is_connected():
        print('Connected to MySQL database')
    else:
        print('Connection to database failed, try later')
    cursor = connection_db.cursor()
    connection_db.commit()
    return connection_db


def visitor_exists(cursor, user_id):
    """Check if there is already a user in the database"""
    data_query = (user_id,)
    query = ("select if( exists(select * from visitors where user_id=%s), 1, 0)")
    cursor.execute(query, data_query)
    user_exist = cursor.fetchone()[0]
    return user_exist


def add_visitor(db, cursor, user_id, user_name, first_name, last_name, date_time):
    """add new visitor"""
    data_query = (user_id, user_name, first_name, last_name, date_time,)
    query = (
        """INSERT INTO visitors (user_id, user_name, user_first_name, user_last_name, date_time) VALUES(%s,%s,%s,%s,%s)""")
    cursor.execute(query, data_query)
    db.commit()
    # cursor.close()
    # db.close()


def add_visitor_phone_number(db, cursor, user_id, user_phone_number):
    """Add phone number of visitor"""
    cursor.execute("""UPDATE visitors SET user_phone_number = %s WHERE user_id = %s""", (user_phone_number, user_id,))
    db.commit()


def add_visitor_need_help(db, cursor, user_id, user_full_name, user_phone_number, date_time, status=False):
    """Add new visitor need help"""
    cursor.execute("""INSERT INTO visitors_need_help (user_id, user_full_name, user_phone_number, date_time, status) VALUES(%s,%s,%s,%s,%s)""", (user_id, user_full_name, user_phone_number, date_time, status, ))
    db.commit()
