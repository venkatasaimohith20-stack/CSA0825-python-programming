BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
DAYS = 10

def calculate_payment(litres, fat, snf):
    """Return the rate per litre and payment for one entry."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE
    rate += snf_steps * SNF_STEP_VALUE
    rate = round(rate, 2)

    amount = round(litres * rate, 2)
    return rate, amount

farmer_id = input("Enter Farmer ID: ")
total = 0.00
for day in range(1, DAYS + 1):
    print(f"\nDay {day}")

    try:
        litres = float(input("Enter litres: "))
        fat = float(input("Enter fat percentage: "))
        snf = float(input("Enter SNF percentage: "))
        shift = input("Enter shift (Morning/Evening): ").strip().title()

        if (litres <= 0 or not 2.0 <= fat <= 7.0
                or not 0 <= snf <= 100
                or shift not in ("Morning", "Evening")):
            print("Invalid entry. Please enter this day again.")
            # Retry the same day
            while True:
                try:
                    litres = float(input("Enter litres: "))
                    fat = float(input("Enter fat percentage: "))
                    snf = float(input("Enter SNF percentage: "))
                    shift = input(
                        "Enter shift (Morning/Evening): "
                    ).strip().title()

                    if (litres > 0 and 2.0 <= fat <= 7.0
                            and 0 <= snf <= 100
                            and shift in ("Morning", "Evening")):
                        break
                    print("Invalid entry. Try again.")
                except ValueError:
                    print("Enter numeric values correctly.")
        rate, amount = calculate_payment(litres, fat, snf)
    except ValueError:
        print("Invalid numeric input. Please restart the program.")
        break
    total = round(total + amount, 2)
    print(f"Rate per litre: Rs. {rate:.2f}")
    print(f"Daily payment: Rs. {amount:.2f}")
    print(f"Running total: Rs. {total:.2f}")
else:
    print("\n--- Ten-Day Payment Summary ---")
    print("Farmer ID:", farmer_id)
    print(f"Total payment: Rs. {total:.2f}")
