# main.py
import logging, sys
import os # Import os for checking .env file

# Import functions from your modules
from connect import create_connection
from delete import delete_customer
from insert import insert_author
from update import update_customer_email
from bulk import bulk_copy_customers
from imports import import_author_from_csv # Renamed to avoid conflict with `import` keyword
from query import find_customer_by_id, get_customers
from transaction import create_order
from procedure import count_customer_by_email_domain # Added procedure.py


# Configure logging to console
logging.basicConfig(
    stream=sys.stdout,
    encoding='utf-8',
    format='%(levelname)s:%(message)s',
    level=logging.DEBUG
)

def main():
    logging.info("--- Starting Database Operations Demonstration ---")

    # 1. Test Database Connection
    logging.info("\n--- Testing Database Connection ---")
    conn = create_connection()
    if conn:
        logging.info("Successfully connected to the database!")
        conn.close()
    else:
        logging.error("Failed to connect to the database. Please check your .env file and SQL Server.")
        return # Exit if connection fails

    # 2. Insert a New Author
    logging.info("\n--- Demonstrating Author Insertion ---")
    # This requires the 'Authors' table to exist.
    author_id = insert_author("Virginia", "Woolf", "1882-01-25")
    if author_id:
        logging.info(f"Inserted author with ID: {author_id}")
    else:
        logging.error("Failed to insert author.")

    # 3. Import Authors from CSV
    logging.info("\n--- Demonstrating Importing Authors from CSV ---")
    # This requires 'authors.csv' to exist in the same directory.
    # Example 'authors.csv' content:
    # FirstName,LastName,BirthDate
    # J.K.,Rowling,1965-07-31
    # George,Orwell,1903-06-25
    try:
        import_author_from_csv(r"C:\Users\Shivam Gupta\OneDrive\Documents\Shivam_Developement\PYTHON\python_tutorial\sqlserver-python\data\authors.csv")
        logging.info("Authors import process completed.")
    except FileNotFoundError:
        logging.error("authors.csv not found. Skipping author import.")
    except Exception as e:
        logging.error(f"Error during author import: {e}")


    # 4. Bulk Copy Customers from CSV
    logging.info("\n--- Demonstrating Bulk Copy Customers ---")
    # This requires 'customers.csv' to exist and the 'Customers' table to match its schema.
    # Example 'customers.csv' content:
    # CustomerID,FirstName,LastName,Email,PhoneNumber,Address
    # 101,Alice,Smith,alice.smith@example.com,111-222-3333,123 Main St
    # 102,Bob,Johnson,bob.j@example.com,444-555-6666,456 Oak Ave
    try:
        if bulk_copy_customers(r"C:\Users\Shivam Gupta\OneDrive\Documents\Shivam_Developement\PYTHON\python_tutorial\sqlserver-python\data\customers.csv"):
            logging.info("Bulk copy of customers successful.")
        else:
            logging.warning("Bulk copy of customers failed or no data. Ensure 'customers.csv' exists and table schema matches.")
    except FileNotFoundError:
        logging.error("customers.csv not found. Skipping bulk copy.")
    except Exception as e:
        logging.error(f"Error during bulk copy: {e}")

    # 5. Find a Customer by ID
    logging.info("\n--- Demonstrating Finding Customer by ID (e.g., ID 101) ---")
    # This assumes customer with ID 101 exists from bulk copy or manual entry.
    customer_101 = find_customer_by_id(101)
    if customer_101:
        logging.info(f"Found customer: {customer_101}")
    else:
        logging.warning("Customer with ID 101 not found.")

    # 6. Update Customer Email
    logging.info("\n--- Demonstrating Updating Customer Email (for ID 101) ---")
    # This assumes customer with ID 101 exists.
    if update_customer_email(101, "alice.updated@example.com"):
        logging.info("Customer 101 email updated successfully.")
        updated_customer = find_customer_by_id(101)
        logging.info(f"Verified updated customer: {updated_customer}")
    else:
        logging.warning("Failed to update customer 101 email (customer might not exist).")

    # 7. Get Customers with Limit and Offset
    logging.info("\n--- Demonstrating Getting Customers (limit 2, offset 0) ---")
    customers_list = get_customers(limit=2, offset=0)
    if customers_list:
        logging.info("First 2 customers:")
        for customer in customers_list:
            logging.info(customer)
    else:
        logging.warning("No customers found or error retrieving them.")

    # 8. Create an Order (Transaction Example)
    logging.info("\n--- Demonstrating Creating an Order (Transaction) ---")
    # This requires 'Inventories', 'Orders', and 'OrderDetails' tables.
    # Also, 'Inventories' should have BookId=1 with sufficient Qty.
    order_successful = create_order(customer_id=101, book_id=1, quantity=1, price=29.99, order_date="2024-05-21")
    if order_successful:
        logging.info("Order created successfully (transaction committed).")
    else:
        logging.warning("Failed to create order (transaction rolled back). Check table setup/inventory.")

    # 9. Count Customers by Email Domain (Stored Procedure)
    logging.info("\n--- Demonstrating Counting Customers by Email Domain ---")
    # This requires a stored procedure named 'CountCustomerByEmailDomain' in your SQL Server.
    # Example SQL Server Stored Procedure:
    # CREATE PROCEDURE CountCustomerByEmailDomain
    #     @Domain NVARCHAR(255),
    #     @Count INT OUTPUT
    # AS
    # BEGIN
    #     SELECT @Count = COUNT(*) FROM Customers WHERE Email LIKE '%' + @Domain;
    # END;
    try:
        domain_count = count_customer_by_email_domain('@example.com')
        logging.info(f"Number of customers with email domain '@example.com': {domain_count}")
    except Exception as e:
        logging.error(f"Error calling stored procedure 'CountCustomerByEmailDomain': {e}. Ensure it exists.")


    # 10. Delete a Customer
    logging.info("\n--- Demonstrating Deleting a Customer (e.g., ID 102) ---")
    # This assumes customer with ID 102 exists.
    rows_deleted = delete_customer(102)
    if rows_deleted > 0:
        logging.info(f"Successfully deleted {rows_deleted} customer(s).")
    else:
        logging.warning("No customer deleted with ID 102 (might not exist).")

    logging.info("\n--- Database Operations Demonstration Complete ---")




if __name__ == "__main__":
    # Check if .env file exists before running
    if not os.path.exists('.env'):
        logging.error("Error: .env file not found. Please create one with DB_SERVER, DB_USER, DB_PASSWORD, DB_NAME.")
    else:
        main()