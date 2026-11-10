def process_mess_bill(file_name):
    total = 0.0
    report = ""
    rejected_lines = []
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                stripped_line = line.strip()
                if not stripped_line:  # Skip empty lines
                    continue
                parts = stripped_line.split(",")
                try:
                    # Expecting: register number, name, amount
                    if len(parts) != 3:
                        raise ValueError("Incorrect number of fields")
                    reg_no, name, amount_str = parts[0].strip(), parts[1].strip(), parts[2].strip()
                    amount = float(amount_str)
                    total += amount
                    report += f"{name} {amount_str}\n"
                except (ValueError, IndexError) as e:
                    rejected_lines.append((line_no, stripped_line, str(e)))
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return
    print("--- Report ---")
    print(report, end="")
    print(f"Total: {total:.2f}")
    print(f"Rejected Lines Count: {len(rejected_lines)}")