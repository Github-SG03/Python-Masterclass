import os

def merge_files_with_os(file1, file2, merged_file):
    with open(merged_file, 'w') as outfile:
        for filename in [file1, file2]:
            with open(filename, 'r') as infile:
                for line in infile:
                    outfile.write(line)

# Usage:
file1 = 'file1.txt'
file2 = 'file2.txt'
merged_file = 'merged_file.txt'
merge_files_with_os(file1, file2, merged_file)