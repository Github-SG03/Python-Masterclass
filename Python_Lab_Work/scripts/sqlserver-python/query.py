import logging
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
                Customers 
            WHERE CustomerID = %s"""
    
    # Execute the query
    with (conn, conn.cursor() as cursor):
        cursor.execute(sql, customer_id)
        row = cursor.fetchone()
        return row
    



def get_customers(limit: int, offset: int = 0) -> list[dict] | None:
    # Connect to the SQL Server
    conn = create_connection()
    if conn is None:
        return None

    sql = f"""SELECT * FROM Customers ORDER BY CustomerID 
            OFFSET %s ROWS FETCH FIRST %s ROWS ONLY"""
    
    # Execute the query
    with (conn, conn.cursor(as_dict=True) as cursor):
        cursor.execute(sql, (offset, limit))
        return cursor.fetchall()