########################################################################################################################################################
import pandas as pd
import pyarrow.parquet as pq

# Path to your .parquet file
file_path = r"C:\Users\Shivam Gupta\OneDrive\Documents\Shivam_Developement\PYTHON\python_tutorial\part-r-00000-1a9822ba-b8fb-4d8e-844a-ea30d0801b9e.gz.parquet"

try:
    # Read the whole Parquet file
    df = pd.read_parquet(file_path, engine="pyarrow")

    # ✅ Display all rows and columns
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)

    # 🔽 Optionally, export to CSV for easier viewing
    #output_csv = file_path.replace(".parquet", ".csv")
    #df.to_csv(output_csv, index=False)
    #print(f"\n✅ Full data exported to: {output_csv}")

except Exception as e:
    print("❌ Error reading Parquet file:")
    print(e)



# Load the Parquet file
parquet_file = pq.ParquetFile(
    r"C:\Users\Shivam Gupta\OneDrive\Documents\Shivam_Developement\PYTHON\python_tutorial\part-r-00000-1a9822ba-b8fb-4d8e-844a-ea30d0801b9e.gz.parquet"
)

print("File metadata:")
print(parquet_file.metadata)

print("\nFirst row group metadata:")
print(parquet_file.metadata.row_group(0))

print("\nFirst column in first row group:")
print(parquet_file.metadata.row_group(0).column(0))

print("\nColumn statistics:")
print(parquet_file.metadata.row_group(0).column(0).statistics)

