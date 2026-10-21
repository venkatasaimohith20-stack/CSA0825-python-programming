
from decimal import Decimal, ROUND_HALF_UP

# Seasonal rate settings
BASE_RATE = Decimal("32.00")
FAT_STEP_RATE = Decimal("0.45")
BONUS_RATE = Decimal("0.50")
BONUS_LIMIT = 500


def get_rate_card(season):
    if season.lower() in ["april", "may", "june"]:
        return BASE_RATE, FAT_STEP_RATE
    else:
        return Decimal("30.00"), Decimal("0.40")


def calculate_rate(fat, snf, season, litres):
    base, step_rate = get_rate_card(season)

    # Example: each 1.00 fat unit above 3.00 earns one step
    fat_steps = max(0, int((fat - Decimal("3.00")).to_integral_value(
        rounding=ROUND_HALF_UP
    )))
    
    rate = base + Decimal(fat_steps) * step_rate

    if litres > BONUS_LIMIT:
        rate += BONUS_RATE

    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


# Input
season = input("Enter season/month: ").strip()
fat = Decimal(input("Enter fat value (e.g. 4.25): "))
snf = Decimal(input("Enter SNF value (e.g. 8.50): "))
litres = Decimal(input("Enter total litres supplied in 10 days: "))

# Calculation
final_rate = calculate_rate(fat, snf, season, litres)

print("\n--- MILK RATE CALCULATOR ---")
print("Season:", season)
print("Fat:", fat)
print("SNF:", snf)
print("Base rate: Rs.", get_rate_card(season)[0])
print("Bonus eligible:", "Yes" if litres > BONUS_LIMIT else "No")
print("Final rate per litre: Rs.", final_rate)
print("Total payment: Rs.", final_rate * litres)
