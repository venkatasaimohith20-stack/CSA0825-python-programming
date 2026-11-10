def compute_daily_summary(readings_list):
    """
    Computes daily summary (min, max, mean, valid count) per station from raw records.
    """
    if not readings_list:
        return {}       
    summary = {}
    for station, date, pm25 in readings_list:
        key = (station, date)
        if key not in summary:
            summary[key] = []
        summary[key].append(pm25)
        
    results = {}
    for (station, date), vals in summary.items():
        results[(station, date)] = {
            "min": min(vals),
            "max": max(vals),
            "mean": sum(vals) / len(vals),
            "valid_readings": len(vals)
        }
    return results
sample_data = [("Adyar", "2026-10-01", 45), ("Adyar", "2026-10-01", 55), ("Guindy", "2026-10-01", 90)]
print(compute_daily_summary(sample_data))