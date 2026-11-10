def get_subsidy_separate(units, has_ration_card, age):
    subsidy_count = 0
    if units <= 100:
        subsidy_count += 1
    if 101 <= units <= 200 and has_ration_card:
        subsidy_count += 1
    if units > 200 and age > 80:
        subsidy_count += 1
    return subsidy_count

def get_subsidy_elif(units, has_ration_card, age):
    if units <= 100:
        return "Full Subsidy"
    elif 101 <= units <= 200:
        return "Partial Subsidy" if has_ration_card else "No Subsidy"
    else:
        return "Special Senior Subsidy" if age > 80 else "No Subsidy"
print("--- Q1 Outputs ---")
print("Input: 90 units, No Card, Age 30 (Separate) ->", get_subsidy_separate(90, False, 30))
print("Input: 150 units, Has Card, Age 40 (Elif)     ->", get_subsidy_elif(150, True, 40))
print("Input: 250 units, No Card, Age 85 (Elif)     ->", get_subsidy_elif(250, False, 85))