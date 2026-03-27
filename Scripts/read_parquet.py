########################################################################################################################################################
from pathlib import Path

import pandas as pd
import pyarrow.parquet as pq

REPO_ROOT = Path(__file__).resolve().parents[2]
PARQUET_CANDIDATES = [
    REPO_ROOT / "Pyspark-HandsOnDatabricks" / "datasets" / "interim" / "parquet_data" / "part-00000-tid-2648944911255100992-3e6ccd82-fe6f-4eb9-bbe8-867d1481eace-462-1.c000.snappy.parquet",
    REPO_ROOT / "SnowflakeMasterClass-Udemy" / "datasets" / "sales_items_data.parquet",
]

file_path = next((path for path in PARQUET_CANDIDATES if path.exists()), None)

if file_path is None:
    print("No local parquet sample found in the repository.")
else:
    try:
        df = pd.read_parquet(file_path)

        with pd.option_context("display.max_rows", None, "display.max_columns", None):
            print(df)

        parquet_file = pq.ParquetFile(file_path)
        print("File metadata:")
        print(parquet_file.metadata)
        print("First row group metadata:")
        print(parquet_file.metadata.row_group(0))
        print("First column in first row group:")
        print(parquet_file.metadata.row_group(0).column(0))
        print("Column statistics:")
        print(parquet_file.metadata.row_group(0).column(0).statistics)
    except Exception as exc:
        print(f"Error reading Parquet file: {exc}")
