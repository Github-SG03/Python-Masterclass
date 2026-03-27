import logging, sys
from connect import create_connection
from insert import insert_author
from import_author import import_author_from_csv
from update import update_customer_email
from query import find_customer_by_id
from delete import delete_customer
from transaction import create_order
from procedure import get_books_by_published_date

# config logging to console
logging.basicConfig(stream=sys.stdout, encoding='utf-8', format='%(levelname)s:%(message)s',level=logging.DEBUG)

# create a database connection
conn = create_connection()
if conn:
    logging.info('Connected to the SQL Server database successfully.')
    conn.close()

# insert a new author
id = insert_author('Alice', 'Johnson', '1978-05-14')
if id is not None:
    logging.info(f'Author ID: {id}')

# import authors from CSV
import_author_from_csv('./data/authors.csv')

# update customer email
update_customer_email(1, 'stephenjohnson@wilson-foster.com')

#customer = find_customer_by_id(1)
customer = find_customer_by_id(1)
print(customer)

# Delete customer with id 1
try:
    row_deleted = delete_customer(1)
    logging.info(f'{row_deleted} row(s) deleted.')
except Exception as e:
    logging.error(f"Error fetching customers: {e}")


# create an order
try:
    create_order(
        customer_id=10,
        book_id=1,
        quantity=15, 
        price=15.99,
        order_date='2024-07-24'
    );
except Exception as e:
    logging.error(f"Error fetching customers: {e}")  

# get books published between two dates
books = get_books_by_published_date('2022-01-01', '2023-12-31')
for book in books: # pyright: ignore[reportOptionalIterable]
    print(f'{book["Title"]} - Published on {book["PublishedDate"]}')