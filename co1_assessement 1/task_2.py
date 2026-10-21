
from decimal import Decimal
import sys

# Explore data types
print("--- Data Types ---")
print(type(10))
print(type(10.0))
print(type("10"))
print(type(True))
print(type([10, 8.5]))

# Explore division operators
print("\n--- Division Operators ---")
print("7 / 2 =", 7 / 2)
print("7 // 2 =", 7 // 2)
print("7 % 2 =", 7 % 2)
print("-7 // 2 =", -7 // 2)

# Floating-point precision
print("\n--- Floating-Point Issue ---")
print("0.1 + 0.2 =", 0.1 + 0.2)
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3)

# Payment amounts stored as strings
payments = ["33.40"] * 1000 + ["0.10"] * 3

def total_float(items):
    total = 0.0
    for amount in items:
        total += float(amount)
    return total

def total_decimal(items):
    total = Decimal("0.00")
    for amount in items:
        total += Decimal(amount)  # TODO 1 completed
    return total

print("\n--- Payment Totals ---")
print("float:", total_float(payments))
print("Decimal:", total_decimal(payments))
print("Decimal comparison:",
      Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

# Compare Decimal(amount) with Decimal(float(amount))
print("\n--- Decimal Conversion ---")
print('Decimal("0.10") =', Decimal("0.10"))
print("Decimal(float('0.10')) =", Decimal(float("0.10")))

# Memory used by one representative value
print("\n--- Memory Usage ---")
print("Integer 10:", sys.getsizeof(10), "bytes")
print("Float 10.0:", sys.getsizeof(10.0), "bytes")
print("Decimal('10.00'):", sys.getsizeof(Decimal("10.00")), "bytes")
