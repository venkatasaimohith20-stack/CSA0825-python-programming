import time
def climb_recursive(n):
    if n <= 1:
        return 1
    return climb_recursive(n - 1) + climb_recursive(n - 2)
def climb_iterative(n):
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
print("--- Q7 Validation Outputs ---")
test_n = 30  # Keep n reasonable for the recursive version so it doesn't hang
start_time = time.perf_counter()
res_rec = climb_recursive(test_n)
time_rec = time.perf_counter() - start_time
start_time = time.perf_counter()
res_iter = climb_iterative(test_n)
time_iter = time.perf_counter() - start_time
print(f"Input n = {test_n}")
print(f"Recursive Result: {res_rec} | Time taken: {time_rec:.6f} seconds")
print(f"Iterative Result: {res_iter} | Time taken: {time_iter:.6f} seconds")
print(f"Performance Speedup: {time_rec / time_iter:.2f}x faster with the iterative redesign!")