# Angstrom Number eg. 153 = 1 cube + 2 cube + 3 cube = 153

num = int(input("Enter Number: "))

a = str(num)

summ = 0

for i in a:
    summ += int(i) ** 3

if summ == num:
    print(num, "is an Angstrom Number.")

else:
    print(num, "is not an Angstrom Number.")