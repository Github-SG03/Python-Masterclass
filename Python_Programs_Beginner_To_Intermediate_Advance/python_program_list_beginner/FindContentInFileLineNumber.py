def find_word_in_file(file_path, target_word):
	try:
		with open(file_path, 'r') as file:
			for line_number, line in enumerate(file, start=1):
				if target_word in line:
					return line_number

	except FileNotFoundError:
		print("Error: The file was not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

	return None # Return None if the word is not found in the file.


# Example usage:
file_path = 'file1.txt'
word_to_find = 'Abhishek'
result = find_word_in_file(file_path, word_to_find)
if result:
	print(f"The word '{word_to_find}' was found in line number: {result}")
else:
	print(f"The word '{word_to_find}' was not found in the file.")
