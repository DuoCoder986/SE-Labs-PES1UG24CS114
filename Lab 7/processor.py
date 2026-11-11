
import math


def parse_application(text):
    # Check input type
    if not isinstance(text, str):
        return None

    # Require exactly one colon
    if text.count(':') != 1:
        return None

    visa, entries = text.split(':')
    visa = visa.strip()
    entries = entries.strip()

    # Both fields must be present
    if not visa or not entries:
        return None

    # Validate entry count
    try:
        entries = int(entries)
    except ValueError:
        return None

    if entries <= 0:
        return None

    return visa.title(), entries


def processing_average(days_csv):
    # Check input type
    if not isinstance(days_csv, str):
        return None

    if not days_csv.strip():
        return None

    try:
        values = [int(r.strip()) for r in days_csv.split(',')]
    except ValueError:
        return None

    # Reject empty or negative values
    if not values or any(day < 0 for day in values):
        return None

    return sum(values) // len(values)


def payable_fee(text):
    # Check input type
    if not isinstance(text, str):
        return None

    # Require exactly one separator
    if text.count('|') != 1:
        return None

    fee, discount = text.split('|')

    try:
        fee = float(fee.strip())
        discount = float(discount.strip())
    except ValueError:
        return None

    # Reject negative and non-finite values
    if not math.isfinite(fee) or not math.isfinite(discount):
        return None

    if fee < 0 or discount < 0:
        return None

    total = fee * 1.18 - discount

    if not math.isfinite(total):
        return None

    return max(total, 0)


def main():
    print("==== Running parse_application ====")
    user_input = input("Enter visa type:entries (e.g. tourist:2): ")
    result = parse_application(user_input)
    print("Visa Type and Entries:", result if result is not None else "Invalid input")

    print("\n==== Running processing_average ====")
    user_input = input("Enter processing days as CSV (e.g. 5,10,21): ")
    result = processing_average(user_input)
    print("Average Processing Days:", result if result is not None else "Invalid input")

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 6000|500): ")
    result = payable_fee(user_input)
    print("Payable Fee:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()
