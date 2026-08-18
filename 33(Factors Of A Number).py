n = int(input("Enter Number: "))

print("Factors of", n, "Are: ")

for i in range(1, n+1):
    if n % i == 0:
        print(i)
    i+=1