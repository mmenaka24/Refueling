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
    xstr, ystr = fraction.split("/")
    x = int(xstr)
    y = int(ystr)
    if y == 0:
        raise ZeroDivisionError
    if not x > y:
        return round((x / y) * 100)
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
