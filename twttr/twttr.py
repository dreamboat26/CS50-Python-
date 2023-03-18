text = input("Enter some text: ")
vowels = "aeiouAEIOU"
output = ""

for char in text:
    if char not in vowels:
        output += char

print(output)
