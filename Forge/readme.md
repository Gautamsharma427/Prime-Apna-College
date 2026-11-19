# Introduction
Forge is a software/Saas which helps businesses of various different categories manage their products,inventory, suppliers and orders.

Imagine a small company that sells electronic products. It needs a central system to:
- Maintain a product catalogue.
- Track inventory.
- Manage suppliers.
- Process customer orders.
- Monitor low-stock products.
- Generate operational reports.
- Eventually automate operations using AI agents.

# Forge Inventory(version 0.1)

A simple command-line inventory management system written in Python. It allows users to track products, check stock levels, update quantities, and identify items that need restocking.

## Features

* **Add Product:** Record new items with a name, SKU, price, current quantity, and reorder level.
* **View All Products:** Display the complete list of stored inventory items.
* **Search Products:** Look up specific product details using its unique SKU.
* **Update Stock:** Modify the available quantity for an existing product by SKU.
* **Low Stock Report:** Automatically filter and display products whose quantity is at or below their reorder level.

## Requirements

* Python 3.x (No external libraries required)

## How to Run

1. Save the code to a file named `forge_inventory.py`.
2. Open your terminal or command prompt and navigate to the file's directory.
3. Run the script using:
   ```bash
   python forge_inventory.py
   ```

## Usage Guide

Once the program starts, select an option from the interactive menu by entering the corresponding number:

```text
==============================
FORGE INVENTORY
==============================
1. Add Product
2. View All Products
3. Search Products
4. Update Stock
5. Low Stock Report
Press -1 to exit
Choose an option: 
```

* **Option `1`:** Prompts you to enter `Product-name`, `SKU`, `Price`, `Quantity`, and `Reorder level`.
* **Option `2`:** Prints all currently saved products as a list of dictionaries.
* **Option `3`:** Prompts for an `SKU` and prints the matching product (or notifies you if not found).
* **Option `4`:** Prompts for an `SKU` and a new integer stock value to overwrite the current quantity.
* **Option `5`:** Outputs all products where `Quantity <= ReorderLevel`.
* **Option `-1`:** Exits the application.

## Limitations & Notes

* **In-Memory Storage:** Product data is stored in a runtime list (`products = []`) and will be reset when the program exits.
* **Input Validation:** Ensure valid numeric values are entered for price, quantity, and reorder levels to avoid runtime `ValueError` exceptions.
