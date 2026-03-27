############################################################
# UNIT TESTING IN PYTHON (BASIC → ADVANCED)
# Learn unittest step by step with examples
############################################################

############################################################
# 1. WHAT IS UNIT TESTING?
# Unit Testing = testing small parts (functions) of code
# to check if they work correctly
############################################################

# Example function to test
def add(a, b):
    return a + b


############################################################
# 2. IMPORT UNITTEST MODULE
############################################################

import unittest

from numpy import subtract


############################################################
# 3. CREATE TEST CLASS
# Must inherit from unittest.TestCase
############################################################

class TestMathOperations(unittest.TestCase):

    ########################################################
    # 4. TEST FUNCTIONS (METHODS)
    # Must start with 'test_'
    ########################################################

    def test_add(self):
        self.assertEqual(add(2, 3), 5)   # check correct output

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


############################################################
# 5. RUN TESTS
############################################################

if __name__ == "__main__":
    unittest.main()


############################################################
# 6. ASSERT METHODS (IMPORTANT)
############################################################

# assertEqual(a, b)        → a == b
# assertNotEqual(a, b)     → a != b
# assertTrue(x)            → x is True
# assertFalse(x)           → x is False
# assertIs(a, b)           → a is b
# assertIsNone(x)          → x is None


############################################################
# 7. MORE EXAMPLES
############################################################

def is_even(num):
    return num % 2 == 0


class TestEven(unittest.TestCase):

    def test_even(self):
        self.assertTrue(is_even(4))

    def test_odd(self):
        self.assertFalse(is_even(5))


############################################################
# 8. SETUP & TEARDOWN (ADVANCED)
############################################################

class TestWithSetup(unittest.TestCase):

    def setUp(self):
        # runs before every test
        print("\nSetting up test...")
        self.x = 10

    def tearDown(self):
        # runs after every test
        print("Cleaning up...")

    def test_value(self):
        self.assertEqual(self.x, 10)


############################################################
# 9. TESTING EXCEPTIONS
############################################################

def divide(a, b):
    return a / b


class TestException(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


############################################################
# 10. SKIPPING TESTS
############################################################

class TestSkip(unittest.TestCase):

    @unittest.skip("Skipping this test")
    def test_skip_example(self):
        self.assertEqual(1, 1)


############################################################
# 11. PARAMETERIZED STYLE (LOOP TESTING)
############################################################

class TestMultiple(unittest.TestCase):

    def test_multiple_values(self):
        cases = [(2, 3, 5), (1, 1, 2), (0, 5, 5)]

        for a, b, result in cases:
            self.assertEqual(add(a, b), result)


############################################################
# 12. IMPORTANT COMMANDS
############################################################

# Run file:
# python unit_testing_learning.py

# Verbose mode:
# python -m unittest -v unit_testing_learning.py


############################################################
# 13. WHY UNIT TESTING?
############################################################

# - Detect bugs early
# - Improve code quality
# - Safe refactoring
# - Used in CI/CD pipelines


############################################################
# END NOTE Unit TESTING
############################################################

print("\n🎉 Unit Testing Learning Completed!")


############################################################
# PYTEST SINGLE FILE (BASIC → ADVANCED)
# Everything in ONE file (functions + tests)
############################################################

############################################################
# 1. FUNCTIONS TO TEST
############################################################

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def is_even_(num):
    return num % 2 == 0

def division(a, b):
    return a / b


############################################################
# 2. IMPORT PYTEST
############################################################

import pytest 


############################################################
# 3. SIMPLE TESTS
############################################################

def test_addition():
    assert addition(2, 3) == 5

def test_subtraction():
    assert subtraction(5, 2) == 3


############################################################
# 4. BOOLEAN TEST
############################################################

def test_is_even_():
    assert is_even_(4) == True
    assert is_even_(5) == False


############################################################
# 5. EXCEPTION TEST
############################################################

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)


############################################################
# 6. PARAMETERIZED TEST (VERY IMPORTANT)
############################################################

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (1, 1, 2),
    (0, 5, 5)
])
def test_add_multiple(a, b, result):
    assert addition(a, b) == result


############################################################
# 7. FIXTURE (SETUP DATA)
############################################################

@pytest.fixture
def sample_data():
    return {"a": 10, "b": 5}


def test_fixture(sample_data):
    assert addition(sample_data["a"], sample_data["b"]) == 15


############################################################
# 8. SKIP TEST
############################################################

@pytest.mark.skip(reason="Skipping example")
def test_skip():
    assert True


############################################################
# 9. MARK TEST (ADVANCED)
############################################################

@pytest.mark.slow
def test_slow():
    assert addition(100, 200) == 300


############################################################
# END NOTE Pytest
############################################################

# Run using:
# pytest -v unit-Testing&Pytest.py

print("\n🎉 Pytest Single File Ready!")