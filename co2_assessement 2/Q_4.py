import time
items = [f"Item{i}:Rs{i % 50}" for i in range(10_000)]
def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text
def build_join(parts):
    return ";".join(parts) + ";"
start = time.perf_counter()
a = build_plus(items)
t_plus = time.perf_counter() - start
start = time.perf_counter()
b = build_join(items)
t_join = time.perf_counter() - start
print("--- Q4 Outputs ---")
print("Same text validation:", a == b)
print(f"Total length: {len(b)}")
print(f"+= operator time : {t_plus:.5f} seconds")
print(f"str.join() time  : {t_join:.5f} seconds")