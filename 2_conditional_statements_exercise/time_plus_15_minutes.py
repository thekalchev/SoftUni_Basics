def main():
    hour = int(input())
    minute = int(input())

    future_minute = (minute + 15) % 60
    future_hour = (hour + (minute + 15) // 60) % 24

    print(f"{future_hour:d}:{future_minute:02d}")


if __name__ == "__main__":
    main()
