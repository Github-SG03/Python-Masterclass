###############################################
# PANDAS COMPLETE LEARNING SCRIPT (BASIC → ADVANCED)
# Author: You 😎
# Purpose: Learn pandas step by step with comments
###############################################

# Import pandas
import pandas as pd

################################################
# 1. WHAT IS PANDAS?
# Pandas is used for data analysis and manipulation.
# It mainly uses 2 data structures:
# 1. Series (1D)
# 2. DataFrame (2D table like Excel)
################################################


################################################
# 2. SERIES (1D DATA STRUCTURE)
################################################

# Creating a Series
data = [10, 20, 30, 40]
s = pd.Series(data)

print("\n--- Series ---")
print(s)

# Access element
print("First element:", s[0])


################################################
# 3. DATAFRAME (2D TABLE)
################################################

# Creating DataFrame using dictionary
data = {
    "Name": ["A", "B", "C"],
    "Age": [20, 25, 30],
    "Marks": [85, 90, 95]
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

# Access column
print("\nNames column:")
print(df["Name"])


################################################
# 4. BASIC OPERATIONS
################################################

print("\n--- Basic Info ---")
print(df.head())      # First 5 rows
print(df.tail())      # Last 5 rows
print(df.shape)       # (rows, columns)
print(df.columns)     # Column names
print(df.dtypes)      # Data types


################################################
# 5. SELECTING DATA
################################################

# Select row using index
print("\nRow 0:")
print(df.loc[0])

# Select multiple columns
print("\nName & Marks:")
print(df[["Name", "Marks"]])


################################################
# 6. FILTERING DATA
################################################

# Get students with Marks > 85
filtered = df[df["Marks"] > 85]

print("\n--- Filtered Data ---")
print(filtered)


################################################
# 7. ADD / MODIFY COLUMN
################################################

# Add new column
df["Grade"] = ["B", "A", "A"]

# Modify column
df["Age"] = df["Age"] + 1

print("\n--- After Adding Column ---")
print(df)


################################################
# 8. DELETE COLUMN
################################################

df = df.drop("Grade", axis=1)

print("\n--- After Deleting Column ---")
print(df)


################################################
# 9. HANDLE MISSING VALUES
################################################

data = {
    "Name": ["A", "B", "C"],
    "Marks": [90, None, 80]
}

df2 = pd.DataFrame(data)

print("\n--- Missing Values ---")
print(df2)

# Fill missing values
df2["Marks"] = df2["Marks"].fillna(0)

print("\nAfter fillna:")
print(df2)


################################################
# 10. GROUPBY (VERY IMPORTANT)
################################################

data = {
    "Dept": ["IT", "HR", "IT", "HR"],
    "Salary": [50000, 40000, 60000, 45000]
}

df3 = pd.DataFrame(data)

# Group by Dept
group = df3.groupby("Dept")["Salary"].mean()

print("\n--- GroupBy ---")
print(group)


################################################
# 11. SORTING
################################################

sorted_df = df.sort_values(by="Marks", ascending=False)

print("\n--- Sorted Data ---")
print(sorted_df)


################################################
# 12. MERGING (JOIN LIKE SQL)
################################################

df_a = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["A", "B"]
})

df_b = pd.DataFrame({
    "ID": [1, 2],
    "Marks": [90, 80]
})

merged = pd.merge(df_a, df_b, on="ID")

print("\n--- Merged Data ---")
print(merged)


################################################
# 13. APPLY FUNCTION
################################################

# Create new column using function
df["Double Marks"] = df["Marks"].apply(lambda x: x * 2)

print("\n--- Apply Function ---")
print(df)


################################################
# 14. READ / WRITE FILES
################################################

# Save to CSV
df.to_csv("output.csv", index=False)

# Read from CSV
df_read = pd.read_csv("output.csv")

print("\n--- Read CSV ---")
print(df_read)


################################################
# 15. DESCRIBE (STATISTICS)
################################################

print("\n--- Describe ---")
print(df.describe())


################################################
# END NOTE
################################################

# Pandas is heavily used in:
# - Data Analysis
# - Data Engineering
# - Machine Learning

# Practice these:
# - filtering
# - groupby
# - merge
# - handling missing values

print("\n🎉 Pandas Learning Completed!")