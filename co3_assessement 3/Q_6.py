timetable = {
    "12635": {
        "name": "Vaigai Express",
        "stations": [
            ("Chennai Egmore", "07:15", "07:20"),
            ("Tambaram", "07:43", "07:45"),
            ("Villupuram", "09:20", "09:25")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
    },
    "12605": {
        "name": "Pallavan Express",
        "stations": [
            ("Chennai Egmore", "06:10", "06:15"),
            ("Tambaram", "06:38", "06:40"),
            ("Villupuram", "08:15", "08:20")
        ],
        "days": {"Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"}
    }
}
def find_trains_at_station(tt, target_station, target_day):
    results = []
    for train_no, details in tt.items():
        if target_day in details["days"]:
            for station, arr, dep in details["stations"]:
                if station.lower() == target_station.lower():
                    results.append((train_no, details["name"], dep))
    return sorted(results, key=lambda x: x[2]) # Sort by departure time
target_stop = "Tambaram"
day = "Mon"
print(f"Trains stopping at {target_stop} on {day}:")
for t in find_trains_at_station(timetable, target_stop, day):
    print(f"Train {t[0]} ({t[1]}) - Departs at {t[2]}")