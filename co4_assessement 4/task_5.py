def read_attendance_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def calculate_percentage(present, total):
    return (present / total * 100) if total > 0 else 0.0

def generate_report(summary):
    return "\n".join([f"{reg}: Present={d['present']}, Absent={d['absent']}" for reg, d in summary.items()])

if __name__ == "__main__":
    print("Single script execution complete.")