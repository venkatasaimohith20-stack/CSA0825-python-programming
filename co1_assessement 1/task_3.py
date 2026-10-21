# Named constants
BASE_RATE = 30.0
FAT_RATE = 0.40
SNF_RATE = 0.30
MIN_FAT = 2.0
MAX_FAT = 7.0
MAX_LITRES = 1000.0

# Rate card
RATE_CARD = {
    "base": BASE_RATE,
    "fat": FAT_RATE,
    "snf": SNF_RATE
}

# Get input
farmer_id = input("Enter Farmer ID: ")
litres = float(input("Enter milk quantity in litres: "))
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))

# Validate and calculate
if litres <= 0 or litres > MAX_LITRES:
    print("Invalid milk quantity.")
elif fat < MIN_FAT or fat > MAX_FAT:
    print("Invalid fat percentage.")
elif snf < 0 or snf > 100:
    print("Invalid SNF percentage.")
else:
    rate = (RATE_CARD["base"]
            + fat * RATE_CARD["fat"]
            + snf * RATE_CARD["snf"])

    amount = litres * rate

    print("\n--- Farmer Payment Details ---")
    print("Farmer ID:", farmer_id)
    print("Rate per litre: Rs.", round(rate, 2))
    print("Amount payable: Rs.", round(amount, 2))

# Dynamic typing
value = 10
print("\nValue:", value, "| Type:", type(value).__name__)

value = "Morning"
print("Value:", value, "| Type:", type(value).__name__)

# Multiple assignment and swapping
a, b = 10, 20
print("\nBefore swapping:", a, b)

a, b = b, a
print("After swapping:", a, b)
