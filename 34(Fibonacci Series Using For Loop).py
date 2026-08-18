n = int(input("Enter Number Till You Want Fibonacci Series: "))

a, b = 0, 1
summ = 0

print("Series:- ")

for i in range(0, n):
    print(a, end=" ")
    summ += a
    a, b = b, a + b

print("\nSum=", summ)