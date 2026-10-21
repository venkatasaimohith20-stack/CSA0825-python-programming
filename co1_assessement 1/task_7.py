"""Rate card of the village milk co-operative (used as a module)."""

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def rate_per_litre(fat, snf):
    """Return the price per litre, rounded to 2 decimal places."""
    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = (
        BASE_RATE
        + fat_steps * FAT_STEP_VALUE
        + snf_steps * SNF_STEP_VALUE
    )
    return round(rate, 2)


def payout(litres, fat, snf):
    """Return the farmer's payment, rounded to 2 decimal places."""
    amount = litres * rate_per_litre(fat, snf)
    return round(amount, 2)


if __name__ == "__main__":
    for litres, fat, snf in [
        (10, 3.5, 8.5),
        (8.5, 4.2, 8.7),
        (12, 3.1, 8.3)
    ]:
        rate = rate_per_litre(fat, snf)
        pay = payout(litres, fat, snf)
        print(
            f"{litres:g} L fat {fat:g} snf {snf:g} "
            f"rate {rate:.2f} pay {pay:.2f}"
        )
