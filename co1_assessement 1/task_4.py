import math

# Named constants
BASE_RATE = 30.0
FAT_STEP_RATE = 0.40
SNF_STEP_RATE = 0.30
STEP_SIZE = 0.1

# Input
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
litres = float(input("Enter milk quantity in litres: "))

# Calculate steps using round()
fat_steps = round((fat - 3.0) / STEP_SIZE)
snf_steps = round((snf - 8.0) / STEP_SIZE)

# Calculate rate and payment
rate = BASE_RATE + fat_steps * FAT_STEP_RATE + snf_steps * SNF_STEP_RATE
amount = litres * rate

print("\n--- Payment Calculation ---")
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre: Rs.", round(rate, 2))
print("Amount payable: Rs.", round(amount, 2))

# Operator precedence
print("\n--- Expression Examples ---")
print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("round((4.2 - 3.5) / 0.1) =", round((4.2 - 3.5) / 0.1))

# Difference between round(), int(), and floor()
x = -3.7
print("\nFor x = -3.7:")
print("round(x) =", round(x))
print("int(x) =", int(x))
print("math.floor(x) =", math.floor(x))

# Comparison chaining and Boolean operators
print("\n--- Validation ---")
print("2.0 <= fat <= 7.0:", 2.0 <= fat <= 7.0)
print("Fat and SNF valid:", 2.0 <= fat <= 7.0 and snf >= 0)

# Three surprising results
print("\n--- Unexpected Results ---")
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)
print("round(2.5) =", round(2.5))
print("int(-3.7) =", int(-3.7))
