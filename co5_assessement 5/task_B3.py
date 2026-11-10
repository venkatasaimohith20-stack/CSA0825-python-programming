import sqlite3
import statistics
import time
data = [
    ("Adyar", "2026-10-01", 45.0),
    ("Adyar", "2026-10-01", 55.0),
    ("Guindy", "2026-10-01", 90.0),
    ("Guindy", "2026-10-01", 100.0)
]
def loop_daily_mean(records):
    grouped = {}
    for station, date, val in records:
        key = (station, date)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(val)
    return {k: sum(v)/len(v) for k, v in grouped.items()}
def sql_daily_mean(records):
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE aq (station TEXT, day TEXT, pm25 REAL)")
    con.executemany("INSERT INTO aq VALUES (?, ?, ?)", records)
    con.commit()  
    cursor = con.execute("SELECT station, day, AVG(pm25) FROM aq GROUP BY station, day")
    res = cursor.fetchall()
    con.close()
    return res
print("Loop Mean:", loop_daily_mean(data))
print("SQL Mean:", sql_daily_mean(data))