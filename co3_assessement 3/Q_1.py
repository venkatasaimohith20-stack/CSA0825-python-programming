import random
random.seed(42)
readings = [random.choice([0, 0, 2, 5, 12, 25, 45, 0]) for _ in range(365)]
weekly_totals = [sum(readings[i:i+7]) for i in range(0, len(readings), 7)]
print("Weekly Totals (first 4 weeks):", weekly_totals[:4])
max_rain = max(weekly_totals)
min_rain = min(weekly_totals)
wettest_week = weekly_totals.index(max_rain) + 1
driest_week = weekly_totals.index(min_rain) + 1
print(f"Wettest Week: Week {wettest_week} ({max_rain} mm)")
print(f"Driest Week: Week {driest_week} ({min_rain} mm)")
def moving_average(data):
    if len(data) < 7:
        return []
    return [sum(data[i:i+7]) / 7 for i in range(len(data) - 6)]
print("Moving Average (first 3 days):", moving_average(readings)[:3])
dry_days = [day + 1 for day, rain in enumerate(readings) if rain == 0]
print(f"Total Dry Days: {len(dry_days)}")