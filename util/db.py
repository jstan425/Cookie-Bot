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
    except sqlite3.Error as e:
        print(e)
        raise(e)
    return conn

def create_table(conn, table_name, columns):
    """Create a table with the given name and columns
    :param conn: Connection object
    :param table_name: a CREATE TABLE statement
    :param columns: List of column names and types, eg. ["id INTEGER", 'name TEXT"]
    :return: True if the table was create successfully, False otherwise
    """
    # Validate input
    if not table_name.isidentifier():
        raise ValueError("Invalid table name")
    for column in columns:
        if not isinstance(column, str):
            raise TypeError("Columns must be strings")
        if not column.isidentifier():
            raise ValueError("Invalid column name")
    
    # Sanitize input
    table_name = sqlite3.escape_identifier(table_name)
    columns = [sqlite3.escape_identifier(column) for column in columns]

    # Create SQL statement
    sql = f"CREATE TABLE {table_name} ({', '.join(columns)})"

    # Execute SQL Statement
    try:
        c = conn.cursor()
        c.execute(sql)
        return True
    except sqlite3.Error as e:
        print(e)
        raise e

def setup_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tempban (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        reason TEXT NOT NULL,
                        start_time DATETIME NOT NULL,
                        end_time DATETIME NOT NULL
                    )''')
    conn.commit()
    cursor.close()
