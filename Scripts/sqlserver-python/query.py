from connect import create_connection


def find_customer_by_id(customer_id: int) -> dict | None:
    # Connect to the SQL Server
    conn = create_connection()
    if conn is None:
        return None

    # Find the customer
    sql = """SELECT 
                CustomerID, FirstName, LastName, Email, PhoneNumber, Address
             FROM 
                CustomerXs 
            WHERE CustomerID = %s"""
    
    # Execute the query
    with (conn, conn.cursor() as cursor):
        cursor.execute(sql, (customer_id,))
        row = cursor.fetchone()
        return row # pyright: ignore[reportReturnType]