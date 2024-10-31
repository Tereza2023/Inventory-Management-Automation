# SKU Lookup Program
# This script allows users to search for a SKU and its available quantity
# by entering the last 6 digits of the product barcode.

# Sample data: List of dictionaries containing SKU, barcode, and quantity
data = [
    {"SKU": "SKU001", "Barcode": "123456789012", "Quantity": 4},
    {"SKU": "SKU002", "Barcode": "234567890123", "Quantity": 13},
    {"SKU": "SKU003", "Barcode": "345678901234", "Quantity": 5},
    {"SKU": "SKU004", "Barcode": "456789012345", "Quantity": 6},
    {"SKU": "SKU005", "Barcode": "567890123456", "Quantity": 5},
    {"SKU": "SKU006", "Barcode": "678901234567", "Quantity": 7},
    {"SKU": "SKU007", "Barcode": "789012345678", "Quantity": 11},
    {"SKU": "SKU008", "Barcode": "890123456789", "Quantity": 2},
    {"SKU": "SKU009", "Barcode": "901234567890", "Quantity": 10},
    {"SKU": "SKU010", "Barcode": "012345678901", "Quantity": 42},
    # Additional sample SKUs can be added here
]

# Function to find SKU by the last 6 digits of the barcode
def find_sku_by_barcode(last_six_digits):
    """
    Searches for an SKU and quantity based on the last 6 digits of a barcode.

    Parameters:
        last_six_digits (str): The last 6 digits of the barcode entered by the user.

    Returns:
        tuple: SKU (str) and Quantity (int) if found, otherwise (None, None).
    """
    for item in data:
        if item["Barcode"].endswith(last_six_digits):
            return item["SKU"], item["Quantity"]
    return None, None

# Main function to handle user input and display the result
def main():
    """
    Main function that prompts the user for input, finds the SKU and quantity,
    and displays the result.
    """
    # Prompt the user to enter the last 6 digits of the barcode
    last_six_digits = input("Enter the last 6 digits of the barcode: ")

    # Find the SKU and quantity
    sku, quantity = find_sku_by_barcode(last_six_digits)

    # Display the result
    if sku:
        print(f"SKU: {sku}, Quantity available: {quantity}")
    else:
        print("Barcode not found.")

# Entry point of the script
if __name__ == "__main__":
    main()

