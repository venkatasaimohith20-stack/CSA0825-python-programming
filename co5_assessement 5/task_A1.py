import sqlite3
def setup_database():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stations (
            station_id TEXT PRIMARY KEY,
            location_name TEXT,
            latitude REAL,
            longitude REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            reading_id INTEGER PRIMARY KEY AUTOINCREMENT,
            station_id TEXT,
            date TEXT,
            hour INTEGER,
            pm25 REAL,
            pm10 REAL,
            no2 REAL,
            temperature REAL,
            FOREIGN KEY (station_id) REFERENCES stations (station_id)
        )
    """)
    conn.commit()
    return conn
db_conn = setup_database()
print("Database and tables created successfully.")
db_conn.close()