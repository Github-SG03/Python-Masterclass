# Custom Exception for invalid marks
class InvalidMarksError(Exception):
    def __init__(self, message="Marks must be between 0 and 100"):
        super().__init__(message)

# Function to calculate grade
def calculate_grade(marks):
    try:
        # Raise an exception if marks are not in the valid range
        if marks < 0 or marks > 100:
            raise InvalidMarksError

        # Grading logic
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

    except InvalidMarksError as e:
        return f"Error: {e}"

# Function to get marks input from the user
def get_student_marks():
    while True:
        try:
            # Input marks
            marks = float(input("Enter marks (0-100): "))
            return marks
        except ValueError:
            # Handle invalid input type
            print("Invalid input. Please enter a numeric value.")

# Main program
if __name__ == "__main__":
    print("Welcome to the Student Grading System!")

    try:
        # Get marks from user
        marks = get_student_marks()

        # Calculate grade
        grade = calculate_grade(marks)
        print(f"Grade: {grade}")

    except Exception as e:
        # General exception handling (unexpected errors)
        print(f"An unexpected error occurred: {e}")
    else:
        # Executes only if no exception occurs
        print("Grading completed successfully.")
    finally:
        # Executes regardless of an exception
        print("Thank you for using the Student Grading System!")
