n = int(input("Enter Number Till You Want Your Fibonacci Series: "))

a, b = 0, 1

for i in range(n):
    print(a, end = " ")
    a, b = b, a + b