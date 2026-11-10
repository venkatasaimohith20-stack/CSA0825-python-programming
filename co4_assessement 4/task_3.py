import os
import tempfile
class InvalidRecord(Exception):
    """Raised when a line of the attendance file is not in the expected format."""
    pass
def parse_line(line):
    """'192311001,2026-10-08,P' -> ('192311001', '2026-10-08', 'P')"""
    parts = line.strip().split(",")
    # TODO 1: Raise InvalidRecord if there are not exactly 3 fields or status is not P/A
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    reg_no, date, status = parts[0].strip(), parts[1].strip(), parts[2].strip()
    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")
    return reg_no, date, status
def summarise(path):
    present, absent, errors = 0, 0, []
    # TODO 2: Open file with 'with', parse each line inside try/except InvalidRecord
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                try:
                    reg_no, date, status = parse_line(line)
                    if status == "P":
                        present += 1
                    elif status == "A":
                        absent += 1
                except InvalidRecord as e:
                    errors.append((line_no, str(e)))
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")       
    return present, absent, errors
data = ("192311001,2026-10-08,P\n192311002,2026-10-08,A\n"
        "192311003,2026-10-08\n192311004,2026-10-08,L\n")
with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as tmp:
    tmp.write(data)
    temp_name = tmp.name
print(summarise(temp_name))
os.remove(temp_name)