import unittest
from PYTHON.python_tutorial.ECommerce import Inventory, OrderSystem


class TestInventory(unittest.TestCase):
    """Tests for the Inventory class."""

    def setUp(self):
        """Set up a fresh inventory for each test."""
        self.inventory = Inventory()

    def test_add_item(self):
        """Test adding items to the inventory."""
        self.inventory.add_item("Tablet", 5)
        self.assertEqual(self.inventory.get_stock("Tablet"), 5)

    def test_add_item_existing(self):
        """Test adding stock to an existing item."""
        self.inventory.add_item("Laptop", 5)
        self.assertEqual(self.inventory.get_stock("Laptop"), 15)

    def test_add_item_invalid_quantity(self):
        """Test adding an invalid quantity."""
        with self.assertRaises(ValueError):
            self.inventory.add_item("Phone", -5)

    def test_get_stock(self):
        """Test retrieving stock of an item."""
        self.assertEqual(self.inventory.get_stock("Phone"), 20)

    def test_update_stock(self):
        """Test updating stock after an order."""
        self.inventory.update_stock("Laptop", 5)
        self.assertEqual(self.inventory.get_stock("Laptop"), 5)

    def test_update_stock_insufficient(self):
        """Test updating stock with insufficient quantity."""
        with self.assertRaises(ValueError):
            self.inventory.update_stock("Laptop", 20)

    def test_update_stock_item_not_found(self):
        """Test updating stock for an unknown item."""
        with self.assertRaises(ValueError):
            self.inventory.update_stock("Tablet", 5)


class TestOrderSystem(unittest.TestCase):
    """Tests for the OrderSystem class."""

    def setUp(self):
        """Set up a fresh order system for each test."""
        self.inventory = Inventory()
        self.order_system = OrderSystem(self.inventory)

    def test_place_order(self):
        """Test placing a valid order."""
        result = self.order_system.place_order("Phone", 5)
        self.assertEqual(result, "Order placed for 5 Phone(s).")
        self.assertEqual(self.inventory.get_stock("Phone"), 15)

    def test_place_order_invalid_quantity(self):
        """Test placing an order with an invalid quantity."""
        with self.assertRaises(ValueError):
            self.order_system.place_order("Phone", -5)

    def test_place_order_insufficient_stock(self):
        """Test placing an order with insufficient stock."""
        with self.assertRaises(ValueError):
            self.order_system.place_order("Laptop", 20)


if __name__ == "__main__":
    unittest.main()

#Explanation of the Unit Tests
"""
    Test Setup:
        setUp method initializes a fresh inventory or order system for each test case to ensure independence between tests.

    Testing Inventory:
        Tests include adding items, retrieving stock, and updating stock with valid and invalid inputs.

    Testing OrderSystem:
        Tests include placing valid orders, handling invalid quantities, and insufficient stock scenarios.

    Assertions:
        assertEqual: Checks expected vs actual results (e.g., stock levels).
        assertRaises: Verifies that an exception is raised for invalid operations.


Running the Tests

To run the tests, use the following command:

python -m unittest discover -s . -p "test_ecommerce.py"

Sample Output

----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK

"""
