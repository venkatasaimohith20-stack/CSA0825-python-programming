import csv
import io
RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,121
"""
def load_clean(text):
    """Returns (station, date, pm25) tuples for valid, non-negative readings <= 999 only."""
    rows = []
    f = io.StringIO(text.strip())
    reader = csv.DictReader(f)    
    for row in reader:
        pm_str = row['pm25'].strip()
        # Skip empty, 'NA', or negative/faulty values
        if not pm_str or pm_str.upper() == 'NA':
            continue
        try:
            val = float(pm_str)
            # Valid range check: non-negative and <= 999
            if 0 <= val <= 999:
                rows.append((row['station'], row['date'], val))
        except ValueError:
            continue         
    return rows
def min_max(values):
    """Scale each value to the range 0-1 using (v - min) / (max - min), rounded to 3 decimals."""
    if not values:
        return []
    mn, mx = min(values), max(values)
    if mn == mx:
        return [0.0 for _ in values]
    return [round((v - mn) / (mx - mn), 3) for v in values]
clean = load_clean(RAW)
print(clean)
print(min_max([pm for _, _, pm in clean]))