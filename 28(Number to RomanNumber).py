num = int(input("Enter Number: "))

romans = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "C"), (50, "L"), (40, "XL"), (10, "X"), (5, "V"), (4, "IV"), (3, "III"), (2, "II"), (1, "I")]

roman_num = ""

if num < 1 or num > 3999:
    print("INVALID INPUT")

else:
    for value, symbol in romans:
        while num >= value:
            roman_num += symbol
            num -= value

    print("Roman Num:", roman_num)