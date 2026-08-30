def prime(n):

    if n < 0:
        return "Enter Positive Number"

    elif 0 < n < 2:
        return "Composite Number"
    
    elif n == 2:
        return "Prime Number"

    elif n == 3:
        return "Prime Number"
    
    else:
        for i in range(2, int(n ** 0.5) + 1):

            if n % i == 0:
                return "Composite Number"

            else:
                return "Prime Number"


print(prime(int(input("Enter Number: "))))