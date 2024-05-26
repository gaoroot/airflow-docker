import pyodbc

def test_ms_access_connection(connection_string):
    try:
        # Using a connection string to connect to MS Access
        conn = pyodbc.connect(connection_string)
        print("Connection was successful.")
    except pyodbc.Error as e:
        print("Connection failed:", e)
    finally:
        conn.close()

def select_from_users(connection_string):
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(row)
    except pyodbc.Error as e:
        print("Error in selecting from users table:", e)
    finally:
        if conn:
            conn.close()

# Example usage
connection_string = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=database.accdb;'
test_ms_access_connection(connection_string)