import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def setup_tables(conn):
    # TODO id should auto incriment
    create_temp_ban_table = """ CREATE TABLE IF NOT EXISTS temp_ban (
                                        id integer PRIMARY KEY,
                                        guild_id integer NOT NULL,
                                        user_id integer NOT NULL,
                                        end_time integer NOT NULL
                                    ); """
    create_table(conn, create_temp_ban_table)
