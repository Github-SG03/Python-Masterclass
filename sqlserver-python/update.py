import logging
from connect import create_connection

def update_customer_email(customer_id: int, email: str) -> bool:
    # Connect to the SQL Server
    conn = create_connection()
    if conn is None:
        return False

    # Update the customer email
    with (conn, conn.cursor() as cursor):
        cursor.execute(
            "UPDATE Customers SET Email = %s WHERE CustomerID = %s",
            (email, customer_id),
        )
        conn.commit()
        logging.info(f'{cursor.rowcount} rows updated successfully.')
        return True if cursor.rowcount == 1 else False

