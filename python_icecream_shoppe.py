import json
from datetime import datetime
# this change was make in the cloud
class IceCream:
    """
    Class representing an ice cream flavor with its properties
    """
    def __init__(self, flavor, price, quantity_in_stock, description=""):
        # Initialize ice cream properties
        self.flavor = flavor
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.description = description
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        """Convert ice cream object to dictionary for JSON storage ON THE FILE SYSTEM"""
        return {
            'flavor': self.flavor,
            'price': self.price,
            'quantity_in_stock': self.quantity_in_stock,
            'description': self.description,
            'created_date': self.created_date
        }
    
    def __str__(self):
        """String representation of ice cream for display"""
        return f"{self.flavor} - ${self.price:.2f} ({self.quantity_in_stock} scoops available)"





class IceCreamInventory:
    """
    Class managing the collection of ice cream flavors
    """
    def __init__(self):
        # Initialize empty inventory
        self.flavors = []
    
    def add_flavor(self, ice_cream):
        """Add a new ice cream flavor to inventory with duplicate checking"""
        # Check for duplicate flavors
        for existing in self.flavors:
            if existing.flavor.lower() == ice_cream.flavor.lower():
                print(f"Error: {ice_cream.flavor} already exists in inventory!")
                return False
        # Add new flavor if no duplicate found
        self.flavors.append(ice_cream)
        print(f"Successfully added {ice_cream.flavor} to inventory.")
        return True
    
    def display_inventory(self):
        """Display current inventory status"""
        if not self.flavors:
            print("Inventory is empty!")
            return
        
        print("\nCurrent Ice Cream Inventory:")
        print("-" * 50)
        for ice_cream in self.flavors:
            print(ice_cream)
        print("-" * 50)




    
    def save_to_file(self, filename="ice_cream_inventory.json"):
        """Save inventory to JSON file with error handling"""
        try:
            with open(filename, 'w') as file:
                # Convert inventory to list of dictionaries
                inventory_data = [ice_cream.to_dict() for ice_cream in self.flavors]
                json.dump(inventory_data, file, indent=4)
            print(f"Inventory successfully saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving inventory: {e}")
            return False
