def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percentage))


def convert(fraction):
    try:
        xstr, ystr = fraction.split("/")
        x = int(xstr)
        y = int(ystr)
    except (ValueError, AttributeError):
        # Raised if the string can't be split or the parts can't be converted
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    if x < 0 or y < 0 or x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
