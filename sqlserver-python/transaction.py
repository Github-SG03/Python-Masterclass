import logging
from connect import create_connection


def create_order(customer_id:int , book_id:int, quantity:int, price:float, order_date:str) -> bool:
    # connect to the SQL Server
    conn = create_connection()
    
    if conn is None:
        return False

    with (conn, conn.cursor() as cursor):
        try:
            # check inventory
            cursor.execute("SELECT Qty FROM Inventories WHERE BookId = %s", (book_id,))
            row = cursor.fetchone()
            if row is None or row[0] < quantity:
                raise Exception("Insufficient inventory")

            # insert into orders
            cursor.execute("INSERT INTO Orders (OrderDate, CustomerId, TotalAmount) VALUES (%s, %s, %s)", (order_date, customer_id, price*quantity))
            order_id = cursor.lastrowid

            # insert into orderDetails
            cursor.execute("INSERT INTO OrderDetails (OrderId, BookId, Quantity, Price) VALUES (%s, %s, %s, %s)", (order_id, book_id, quantity, price))

            # update inventories
            cursor.execute("UPDATE Inventories SET Qty = Qty - %s WHERE BookId = %s", (quantity, book_id))
            
            conn.commit()        
            return True
        except Exception as e:
            logging.error(f"Error creating order: {e}")
            conn.rollback()

    return False 