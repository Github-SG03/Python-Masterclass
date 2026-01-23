import re

def is_valid_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[@#$%^&+=]", password):
        return False
    return True

def main():
    password = input("Enter a password to check its validity: ")
    if is_valid_password(password):
        print("The password is valid to use.")
    else:
        print("The password is invalid.")

if __name__ == "__main__":
    main()