BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
MIN_FAT = 2.0
MAX_FAT = 7.0
def calculate_payment(litres, fat, snf):
    """Calculate the milk rate and payment after validating inputs."""

    if litres <= 0:
        raise ValueError("Litres must be greater than zero")

    if not MIN_FAT <= fat <= MAX_FAT:
        raise ValueError("Fat must be between 2.0 and 7.0")

    if not 0 <= snf <= 100:
        raise ValueError("SNF must be between 0 and 100")

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )

    rate = round(rate, 2)
    amount = round(litres * rate, 2)

    return rate, amount


def run_tests():
    """Test valid and invalid payment entries."""

    valid_tests = [
        ("Standard", 10, 3.5, 8.5, 30.00, 300.00),
        ("Above standard", 10, 4.0, 8.7, 32.60, 326.00),
        ("Below standard", 10, 3.0, 8.3, 27.40, 274.00),
        ("Minimum fat", 10, 2.0, 8.5, 24.00, 240.00),
        ("Maximum fat", 10, 7.0, 8.5, 44.00, 440.00),
    ]

    print("--- VALID TESTS ---")

    for name, litres, fat, snf, expected_rate, expected_amount in valid_tests:
        rate, amount = calculate_payment(litres, fat, snf)

        assert rate == expected_rate, f"{name}: incorrect rate"
        assert amount == expected_amount, f"{name}: incorrect payment"

        print(
            f"{name}: Expected = Rs. {expected_amount:.2f}, "
            f"Actual = Rs. {amount:.2f} : PASS"
        )

    invalid_tests = [
        ("Negative litres", -1, 3.5, 8.5),
        ("Zero litres", 0, 3.5, 8.5),
        ("Fat below minimum", 10, 1.9, 8.5),
        ("Fat above maximum", 10, 7.1, 8.5),
        ("Negative SNF", 10, 3.5, -1),
    ]

    print("\n--- INVALID TESTS ---")

    for name, litres, fat, snf in invalid_tests:
        try:
            calculate_payment(litres, fat, snf)
        except ValueError:
            print(f"{name}: Correctly rejected - PASS")
        else:
            raise AssertionError(f"{name}: should have been rejected")

    # Test text conversion
    print("\n--- TEXT INPUT TEST ---")

    try:
        float("eight")
    except ValueError:
        print("Text 'eight': Correctly rejected - PASS")

    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    run_tests()
