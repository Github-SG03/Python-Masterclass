# procedure.py
import logging
from connect import create_connection


def count_customer_by_email_domain(domain: str) -> int:
    # Connect to the SQL Server
    conn = create_connection()

    if conn is None:
        logging.error("Failed to connect to the database in count_customer_by_email_domain.")
        return 0

    try:
        # Use conn.cursor() directly in the with statement
        with conn.cursor() as cursor:
            # When calling stored procedures with OUTPUT parameters
            # and no SELECT result set from the procedure itself:
            # 1. Pass None for the output parameter in callproc.
            # 2. After callproc, the output parameter values are typically
            #    available via cursor.nextset() or by iterating over cursor.stored_results
            #    or sometimes directly on the cursor object itself for the last call.

            # For pymssql specifically, the way to get output parameters
            # for procedures that don't return a result set is to
            # explicitly get the results from cursor.nextset() or by checking
            # the last value of the parameters passed to callproc.
            # However, the most robust way is to make the stored procedure
            # return the output parameter as a simple SELECT result.

            # Let's modify the SQL Stored Procedure to *return* the value
            # as a single-row, single-column result set.
            # This is generally more compatible and easier to retrieve in pymssql.
            # So, the SQL SP from previous step was correct for the DB, but not
            # for simple retrieval via fetchone() unless you make a SELECT.

            # Revert the procedure.py call to expect a SELECT result from the SP
            # The *correct* way to handle the output parameter in pymssql for
            # a procedure that doesn't return a SELECT is trickier.
            # The most common pattern is for the SP to always end with a SELECT.

            # Given your current SP (which calculates @Count and assigns it),
            # the easiest way to retrieve it is to make the SP SELECT that @Count.
            # I will assume your SQL SP is now:
            # SELECT @Count AS CustomerCount;
            # at the end of the SP.

            # Execute the stored procedure
            cursor.callproc('CountCustomerByEmailDomain', (domain, None)) # Pass None for output parameter

            # Fetch the result. If the SP does a final SELECT, this will work.
            row = cursor.fetchone()
            if row:
                return row[0] # Return the first column of the fetched row
            else:
                logging.warning("No result returned from CountCustomerByEmailDomain. Check SP logic or data.")
                return 0

    except Exception as e:
        logging.error(f"Error calling stored procedure 'CountCustomerByEmailDomain': {e}")
        return 0
    finally:
        if conn:
            conn.close() # Ensure connection is closed after use








"""
-- Check if the procedure already exists. If so, drop it.
IF OBJECT_ID('dbo.CountCustomerByEmailDomain', 'P') IS NOT NULL
    DROP PROCEDURE dbo.CountCustomerByEmailDomain;
GO

-- Now, create the procedure
CREATE PROCEDURE dbo.CountCustomerByEmailDomain
    @Domain NVARCHAR(255),
    @Count INT OUTPUT -- This specifies it's an OUTPUT parameter
AS
BEGIN
    -- Assign the count to the output parameter
    SELECT @Count = COUNT(*) FROM Customers WHERE Email LIKE '%' + @Domain;

    -- *** ADD THIS LINE ***
    -- Return the output parameter as a result set, which Python can easily fetch.
    SELECT @Count AS CustomerCount;
END;
GO

--How to test this SP in SSMS (this test script will also work the same way):
DECLARE @ResultCount INT;
EXEC dbo.CountCustomerByEmailDomain @Domain = '@example.com', @Count = @ResultCount OUTPUT;
SELECT @ResultCount AS CustomerCount;


"""