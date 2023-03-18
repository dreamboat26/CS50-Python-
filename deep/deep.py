def main():
    user_input = input("Type something: ")
    if "42" in user_input or "forty-two" in user_input or "Forty Two" in user_input:
        print("Yes")
    else:
        print("No")

main()
