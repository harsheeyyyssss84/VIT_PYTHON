n = int(input("Enter Number: "))

summ = 0

if n < 0:
    print("Enter Positive Number")
elif n == 0:
    print("0")
else:
    for i in range(0, n+1, 1):
        summ+=i
        i+=1

print("Sum of n Natural Numbers is:", summ)