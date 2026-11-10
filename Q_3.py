def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()
def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    if len(reg) == 9:
        return reg[0:2].isalpha() and reg[2:4].isdigit() and reg[4:5].isalpha() and reg[5:9].isdigit()
    else:
        return reg[0:2].isalpha() and reg[2:4].isdigit() and reg[4:6].isalpha() and reg[6:10].isdigit()
def format_number(reg):
    if len(reg) == 9:
        return f"{reg[0:2]} {reg[2:4]} {reg[4:5]} {reg[5:9]}"
    elif len(reg) == 10:
        return f"{reg[0:2]} {reg[2:4]} {reg[4:6]} {reg[6:10]}"
    return reg

# --- Test Inputs & Outputs ---
print("--- Q3 Outputs ---")
test_inputs = ["tn 09 ab 1234", "KA-01-M-0007", "TN9AB1234", "TN 22 1234 AB"]
for raw in test_inputs:
    reg = normalise(raw)
    status = "valid" if is_valid(reg) else "INVALID"
    formatted = format_number(reg) if status == "valid" else "INVALID"
    print(f"{raw:15} -> {reg:11} {status:7} | Format: {formatted}")