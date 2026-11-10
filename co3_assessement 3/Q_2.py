rows, cols = 3, 4

# TODO 1: Create an independent rows x cols grid of zeros using list comprehension
good = [[0 for _ in range(cols)] for _ in range(rows)]

good[0][1] = 7
print("good:", good)
print("Are row 0 and row 1 the same object?:", good[0] is good[1])

# Tuples as dictionary keys (lists are unhashable/mutable, so they raise a TypeError)
stops = {(13.0827, 80.2707): "Chennai Central", (13.0418, 80.2341): "T. Nagar"}
print("Stop name:", stops[(13.0418, 80.2341)])