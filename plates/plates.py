def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

# Checks if only valid characters and length is in the plate
    if s.isalnum() == False or len(s) < 2 or len(s) > 6:
        return False

# Checks if the first two are letters
    for i in range(2):
        if s[i].isalpha() == False: # if it is not letters, return false
            return False

# Checks if the first number is a zero or not (it should not be)
    temp = ""
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            temp += s[i]
            if temp[0] == "0":
                return False

# Edge case: if the whole string is purely letters
    if s.isalpha():
        return True

# Checks if numbers are used in the middle of the plate or not (it should not be)
    for i in range(0, len(s)):
        if s[i].isalpha() == False:
            recorder = i
            break
    valid = True
    for i in range(recorder, len(s)):
        if s[i].isalpha():
            valid = False

    if valid == False:
        return False
    return True

main()
