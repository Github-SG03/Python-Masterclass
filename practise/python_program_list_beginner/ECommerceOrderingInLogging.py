import logging
import os

# Configure logging
LOG_FILE = "ecommerce_system.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Simulated inventory
inventory = {
    "Laptop": 10,
    "Phone": 20,
    "Headphones": 50,
}

class OrderSystem:
    """A class to represent an order system."""

    @staticmethod
    def place_order(item, quantity):
        """Place an order for a specific item."""
        if item not in inventory:
            logging.error(f"Order failed: {item} is not available in inventory.")
            return f"Error: Item '{item}' not found in inventory."

        if quantity <= 0:
            logging.warning(f"Invalid order quantity: {quantity} for item {item}.")
            return "Error: Quantity must be greater than zero."

        if inventory[item] < quantity:
            logging.error(f"Order failed: Insufficient stock for {item}. Requested: {quantity}, Available: {inventory[item]}.")
            return "Error: Insufficient stock."

        # Deduct inventory
        inventory[item] -= quantity
        logging.info(f"Order placed successfully: {quantity} {item}(s). Remaining stock: {inventory[item]}.")
        return f"Success: Ordered {quantity} {item}(s). Remaining stock: {inventory[item]}."

    @staticmethod
    def check_inventory():
        """Log the current inventory status."""
        logging.debug("Checking inventory...")
        return inventory


# Main program to demonstrate the order system
if __name__ == "__main__":
    logging.info("E-commerce Order Processing System started.")

    # List of orders to process
    orders = [
        ("Laptop", 2),
        ("Phone", 25),  # Will fail due to insufficient stock
        ("Tablet", 1)   # Will fail because the item doesn't exist
    ]

    # Process each order
    for item, qty in orders:
        result = OrderSystem.place_order(item, qty)
        print(result)  # Display the result of each order

    # Log the final inventory status
    logging.info("Final inventory status:")
    final_inventory = OrderSystem.check_inventory()
    for item, qty in final_inventory.items():
        logging.info(f"{item}: {qty}")

    # Display log file content (optional)
    if os.path.exists(LOG_FILE):
        print("\n--- Log File Content ---")
        with open(LOG_FILE, 'r') as log_file:
            print(log_file.read())
