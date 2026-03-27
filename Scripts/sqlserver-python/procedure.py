from connect import create_connection

def get_books_by_published_date(start_date: str, end_date: str) -> list[dict] | None:
    # Connect to the SQL Server
    conn = create_connection()
    if conn is None:
        return None
    
    # Call the stored procedure
    with (conn, conn.cursor(as_dict=True) as cursor):
        cursor.callproc('GetBooksByPublishedDate', (start_date, end_date))
        return cursor.fetchall() # type: ignore