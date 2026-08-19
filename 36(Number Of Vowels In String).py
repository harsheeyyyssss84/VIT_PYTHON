string = str(input("Enter String: "))

vowels = "AEIOUaeiou"

num = 0

for ch in string:
    if ch in vowels:
        num += 1

print("Number Of Vowels In Your Line Is/Are:", num)