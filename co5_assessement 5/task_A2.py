def clean_pm25_reading(value, previous_valid_value):
    """
    Cleans an individual PM2.5 reading according to defined rules:
    - If empty or 'NA', use the previous valid value (forward fill).
    - If negative or impossible (> 999), treat as invalid and skip/replace.
    """
    if value is None or str(value).strip().upper() in ("", "NA"):
        return previous_valid_value   
    try:
        val = float(value)
        if 0 <= val <= 999:
            return val
    except ValueError:
        pass   
    return None  # Drop or mark invalid if it fails bounds check

def min_max_normalize(values):
    """Applies min-max scaling to a list of numerical readings."""
    if not values:
        return []
    min_val, max_val = min(values), max(values)
    if min_val == max_val:
        return [0.0 for _ in values]
    return [round((v - min_val) / (max_val - min_val), 3) for v in values]
print(clean_pm25_reading("NA", 45.0))  # Forward fill output: 45.0
print(min_max_normalize([20, 50, 100]))  # Scaling output: [0.0, 0.375, 1.0]