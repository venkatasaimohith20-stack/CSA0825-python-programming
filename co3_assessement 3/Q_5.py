readings = [45, 55, -60, 5, 25, 3, -2, 100]

# 1. Clean and convert to Fahrenheit using list comprehensions with conditions
valid_celsius = [c for c in readings if -50 <= c <= 50]
valid_fahrenheit = [(c * 9/5) + 32 for c in readings if -50 <= c <= 50]

# 2. List of alarm indices where temp was outside 2 to 8 °C
alarm_minutes = [index for index, temp in enumerate(readings) if not (2 <= temp <= 8)]

print("Valid Celsius:", valid_celsius)
print("Valid Fahrenheit:", valid_fahrenheit)
print("Alarm Minutes/Indices:", alarm_minutes)