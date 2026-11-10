def add_item_buggy(item, order=[]):
    order.append(item)
    return order
def add_item(item, order=None):
    if order is None:
        order = []
    order.append(item)
    return order
print("--- Q5 Outputs ---")
print("Buggy sequential calls:")
print("Customer 1:", add_item_buggy("Tea"))
print("Customer 2 (unintended carryover):", add_item_buggy("Vada"))
print("\nCorrected sequential calls:")
print("Customer 1:", add_item("Tea"))
print("Customer 2 (independent list):", add_item("Vada"))