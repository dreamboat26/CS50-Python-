def main():
    time = input("Enter a time (in 24-hour format): ")
    converted_time = convert(time)

    if 7 <= converted_time < 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time < 19:
        print("dinner time")

def convert(time):
    hour, minute = map(int, time.split(":"))
    return hour + minute / 60

if __name__ == "__main__":
    main()

