def main():
    while True:
        try:
            fraction = input("Enter a fraction in the format X/Y: ")
            x, y = map(int, fraction.split('/'))
            if y == 0 or x > y:
                print("Invalid fraction. Please try again.")
                continue
            percentage = round((x / y) * 100)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        except (ValueError, ZeroDivisionError):
            continue


if __name__ == "__main__":
    main()
