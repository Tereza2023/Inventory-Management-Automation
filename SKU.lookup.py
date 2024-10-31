# Define the SKU, barcodes, and quantities in a dictionary
data = [
    {"SKU": "BDV", "Barcode": "634154862377", "Quantity": 4},
    {"SKU": "BMSD", "Barcode": "634154599594", "Quantity": 13},
    {"SKU": "CASEM", "Barcode": "3760349920618", "Quantity": 5},
    {"SKU": "CASETRI", "Barcode": "3760349920625", "Quantity": 6},
    {"SKU": "EBZ", "Barcode": "634154862339", "Quantity": 5},
    {"SKU": "GBUS1", "Barcode": "635131808289", "Quantity": 7},
    {"SKU": "GBUS2", "Barcode": "634154862544", "Quantity": 11},
    {"SKU": "HCO-SUN", "Barcode": "3760349920472", "Quantity": 2},
    {"SKU": "HCO-SUNP", "Barcode": "3760349920830", "Quantity": 10},
    {"SKU": "HLBN", "Barcode": "634154862537", "Quantity": 42},
    {"SKU": "HLG", "Barcode": "634154862407", "Quantity": 51},
    {"SKU": "HLG-BIO", "Barcode": "3760349921417", "Quantity": 1},
    {"SKU": "HLG-C", "Barcode": "3760349920045", "Quantity": 17},
    {"SKU": "HLG-C-BIO", "Barcode": "3760349921424", "Quantity": 1},
    {"SKU": "HLG-DE", "Barcode": "", "Quantity": 7},
    {"SKU": "HLG-S", "Barcode": "617270212073", "Quantity": 14},
    {"SKU": "HLG-S-C", "Barcode": "3760349920311", "Quantity": 6},
    {"SKU": "HLG-SUN", "Barcode": "3760349920458", "Quantity": 10},
    {"SKU": "HLG-SUNP", "Barcode": "3760349920878", "Quantity": 2},
    {"SKU": "HLGM", "Barcode": "3760349920052", "Quantity": 5},
    {"SKU": "HLGM-C", "Barcode": "3760349920069", "Quantity": 6},
    {"SKU": "HLGR (B)", "Barcode": "3760349920021", "Quantity": 6},
    {"SKU": "HLGR (O)", "Barcode": "3760349920038", "Quantity": 10},
    {"SKU": "HLGR-C (B)", "Barcode": "3760349920991", "Quantity": 9},
    {"SKU": "HLGR-SUN (B)", "Barcode": "3760349921004", "Quantity": 20},
    {"SKU": "HLGX", "Barcode": "3760349920724", "Quantity": 2},
    {"SKU": "HLSH", "Barcode": "3760349920007", "Quantity": 10},
    {"SKU": "HLSH-C", "Barcode": "3760349920014", "Quantity": 10},
    {"SKU": "OC (T)", "Barcode": "3760349920410", "Quantity": 9},
    {"SKU": "OC (W)", "Barcode": "3760349920403", "Quantity": 6},
    {"SKU": "OC-SUNP (W)", "Barcode": "3760349920960", "Quantity": 2},
    {"SKU": "OLN", "Barcode": "634154862414", "Quantity": 59},
    {"SKU": "OLN-A", "Barcode": "3760349920427", "Quantity": 41},
    {"SKU": "OLN-A-BIO", "Barcode": "3760349921431", "Quantity": 1},
    {"SKU": "OLN-BIO", "Barcode": "3760349921448", "Quantity": 2},
    {"SKU": "OLN-SUN", "Barcode": "3760349920465", "Quantity": 44},
    {"SKU": "OLN-SUN (PK)", "Barcode": "3760349921011", "Quantity": 1},
    {"SKU": "OLN-SUNP", "Barcode": "3760349920861", "Quantity": 3},
    {"SKU": "OLNR", "Barcode": "3760349920748", "Quantity": 8},
    {"SKU": "OLNR-C", "Barcode": "3760349920755", "Quantity": 5},
    {"SKU": "OLVL", "Barcode": "617270212066", "Quantity": 17},
    {"SKU": "OLVS", "Barcode": "617270212059", "Quantity": 2},
    {"SKU": "OND", "Barcode": "", "Quantity": 1},
    {"SKU": "ORE (B)", "Barcode": "3760349920366", "Quantity": 11},
    {"SKU": "ORE (T)", "Barcode": "3760349920373", "Quantity": 7},
    {"SKU": "ORE-K (G)", "Barcode": "3760349920328", "Quantity": 4},
    {"SKU": "ORE-K (O)", "Barcode": "3760349920335", "Quantity": 20},
    {"SKU": "ORO (G)", "Barcode": "3760349920380", "Quantity": 13},
    {"SKU": "ORO (SB)", "Barcode": "3760349920397", "Quantity": 12},
    {"SKU": "ORO-K (G)", "Barcode": "3760349920342", "Quantity": 7},
    {"SKU": "ORO-K (O)", "Barcode": "3760349920359", "Quantity": 10},
    {"SKU": "ORO-SUN (SB)", "Barcode": "3760349920816", "Quantity": 1},
    {"SKU": "ORO-SUNP (G)", "Barcode": "3760349920809", "Quantity": 1},
    {"SKU": "OSLND", "Barcode": "617270212042", "Quantity": 7},
    {"SKU": "ZED", "Barcode": "", "Quantity": 2},
    {"SKU": "ZEK", "Barcode": "", "Quantity": 1},
    {"SKU": "ZGE", "Barcode": "", "Quantity": 12},
    {"SKU": "ZNB1", "Barcode": "", "Quantity": 17},
    {"SKU": "ZNB2", "Barcode": "", "Quantity": 1}
]

# Function to find SKU by the last 6 digits of the barcode
def find_sku_by_barcode(last_six_digits):
    for item in data:
        if item["Barcode"].endswith(last_six_digits):
            return item["SKU"], item["Quantity"]
    return None, None

# Main function
def main():
    # Input the last 6 digits of the barcode
    last_six_digits = input("Enter the last 6 digits of the barcode: ")

    # Find the SKU and quantity
    sku, quantity = find_sku_by_barcode(last_six_digits)

    if sku:
        print(f"SKU: {sku}, Quantity available at Tereza's home: {quantity}")
    else:
        print("Barcode not found.")

if __name__ == "__main__":
    main()
    
