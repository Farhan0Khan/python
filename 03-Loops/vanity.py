def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(v):
    # Must contain 2–6 characters
    if not 2 <= len(v) <= 6:
        return False

    # Must start with at least two letters
    if not v[0].isalpha() or not v[1].isalpha():
        return False

    # Only letters and numbers are allowed
    if not v.isalnum():
        return False

    # Numbers must be at the end
    number_started = False

    for i in v:
        if i.isdigit():
            if not number_started:
                number_started = True

                # The first number cannot be 0
                if i == '0':
                    return False
        elif number_started:
            # A letter cannot appear after a number
            return False

    return True


main()