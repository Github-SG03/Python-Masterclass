import pyodbc

# Database connection parameters
server = 'localhost\\SQLEXPRESS'
database = 'AdventureWorks2022'
username = 'sgs@sqlserver'
password = 'sgs99@sqlserver'

# Establishing the connection
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=' + server + ';'
                      'DATABASE=' + database + ';'
                      'UID=' + username + ';'
                      'PWD=' + password)

cursor = conn.cursor()

"""
# Create operation
def create_record():
    cursor.execute("INSERT INTO your_table_name (column1, column2) VALUES (?, ?", ('value1', 'value2'))
    conn.commit()
"""


# Read operation
def read_records():
    cursor.execute("SELECT top 10 * FROM Person.Person")
    for row in cursor.fetchall():
        print(row)

"""
# Update operation
def update_record():
    cursor.execute("UPDATE your_table_name SET column1 = ? WHERE column2 = ?", ('new_value', 'value2'))
    conn.commit()
"""


"""
# Delete operation
def delete_record():
    cursor.execute("DELETE FROM your_table_name WHERE column1 = ? ", ('value1',))
    conn.commit()
"""

# Example usage
#create_record()
read_records()
#update_record()
#read_records()
#delete_record()
#read_records()

# Closing the connection AFTER all operations
conn.close()