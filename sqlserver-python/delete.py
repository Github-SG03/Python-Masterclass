from connect import create_connection

def delete_customer(id: int) -> int:
    # Connect to the SQL Server
    conn = create_connection()
    if conn is None:
        return 0
    
    # Delete the customer    
    with (conn, conn.cursor() as cursor):
        cursor.execute("DELETE FROM Customers WHERE CustomerID = %s", (id,))
        conn.commit()
        return cursor.rowcount