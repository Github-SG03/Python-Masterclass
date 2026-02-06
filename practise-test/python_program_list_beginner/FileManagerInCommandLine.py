import argparse
import os

# Function to create a new file
def create_file(file_name):
    if os.path.exists(file_name):
        return f"Error: The file '{file_name}' already exists."
    with open(file_name, 'w') as file:
        file.write("")  # Create an empty file
    return f"File '{file_name}' created successfully."

# Function to append content to a file
def append_to_file(file_name, content):
    if not os.path.exists(file_name):
        return f"Error: The file '{file_name}' does not exist."
    with open(file_name, 'a') as file:
        file.write(content + '\n')
    return f"Content appended to '{file_name}'."

# Function to read content from a file
def read_file(file_name):
    if not os.path.exists(file_name):
        return f"Error: The file '{file_name}' does not exist."
    with open(file_name, 'r') as file:
        content = file.read()
    return f"Content of '{file_name}':\n{content}"

# Main function to parse command-line arguments and execute actions
def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Command-Line File Manager")
    
    # Add arguments for actions
    parser.add_argument("action", choices=["create", "append", "read"], help="Action to perform on the file")
    parser.add_argument("file_name", help="Name of the file to process")
    parser.add_argument("--content", help="Content to append to the file (only for 'append' action)", default="")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Perform the specified action
    if args.action == "create":
        result = create_file(args.file_name)
    elif args.action == "append":
        result = append_to_file(args.file_name, args.content)
    elif args.action == "read":
        result = read_file(args.file_name)
    else:
        result = "Invalid action."

    # Print the result
    print(result)

# Entry point for the program
if __name__ == "__main__":
    main()
