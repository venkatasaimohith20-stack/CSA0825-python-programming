
import time

start = time.perf_counter()

# Co-operative product rates
rates = {
    "Milk": 42.567,
    "Rice": 55.234,
    "Sugar": 38.999,
    "Oil": 120.456
}

print("CO-OPERATIVE RATE CALCULATOR")
print("----------------------------")

for item, rate in rates.items():
    final_rate = round(rate, 2)
    print(item, "Original Rate:", rate,
          "Final Rate:", final_rate)

end = time.perf_counter()

print("\nStart-up and calculation time:",
      round(end - start, 6), "seconds")

print("\nRecommendation:")
print("Round rates to 2 decimal places.")
print("Update rates when prices change.")
print("This program is suitable for small co-operatives.")
