
# Milk Farmer Payment System

# Named constants
BASE_RATE = 30.0
EXTRA_FAT_RATE = 2.0
STANDARD_FAT = 3.0
MIN_FAT = 2.0
MAX_FAT = 7.0
DAYS = 10

# Inputs
farmer_id = input("Enter Farmer ID: ")
litres = float(input("Enter milk quantity in litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
shift = input("Enter shift (Morning/Evening): ").strip().title()

# Validation
if litres <= 0:
    print("Error: Litres must be greater than zero.")
elif fat < MIN_FAT or fat > MAX_FAT:
    print("Error: Fat percentage must be between 2% and 7%.")
elif snf < 0 or snf > 100:
    print("Error: SNF percentage must be between 0 and 100.")
elif shift not in ["Morning", "Evening"]:
    print("Error: Enter Morning or Evening.")
else:
    # Payment calculation
    extra_fat = max(0, fat - STANDARD_FAT)
    rate = BASE_RATE + (extra_fat * EXTRA_FAT_RATE)
    amount = litres * rate

    # Assumption: same quantity and rate for 10 days
    ten_day_total = amount * DAYS

    # Outputs
    print("\n--- Farmer Payment Details ---")
    print("Farmer ID:", farmer_id)
    print("Milk Quantity:", litres, "litres")
    print("Fat Percentage:", fat, "%")
    print("SNF Percentage:", snf, "%")
    print("Shift:", shift)
    print("Rate per Litre: Rs.", round(rate, 2))
    print("Amount Payable: Rs.", round(amount, 2))
    print("Ten-Day Total: Rs.", round(ten_day_total, 2))
