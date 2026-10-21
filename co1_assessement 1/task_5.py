def read_number(prompt):
    while True:
        text = input(prompt).strip()

        # Accept decimal point or decimal comma
        text = text.replace(",", ".")

        try:
            return float(text)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Read clerk's entries
farmer_id = input("Enter Farmer ID: ")
litres = read_number("Enter milk quantity in litres: ")
fat = read_number("Enter fat percentage: ")
snf = read_number("Enter SNF percentage: ")

# Validate values
if litres <= 0:
    print("Error: Milk quantity must be greater than zero.")
elif not (2.0 <= fat <= 7.0):
    print("Error: Fat must be between 2.0 and 7.0.")
elif not (0 <= snf <= 100):
    print("Error: SNF must be between 0 and 100.")
else:
    # Example payment formula
    rate = 30.0 + fat * 0.40 + snf * 0.30
    amount = litres * rate

    print("\n--- Farmer Payment Receipt ---")
    print(f"{'Farmer ID:':<22}{farmer_id}")
    print(f"{'Milk quantity:':<22}{litres:>8.2f} litres")
    print(f"{'Fat percentage:':<22}{fat:>8.2f}%")
    print(f"{'SNF percentage:':<22}{snf:>8.2f}%")
    print(f"{'Rate per litre:':<22}Rs. {rate:>8.2f}")
    print(f"{'Amount payable:':<22}Rs. {amount:>8.2f}")
