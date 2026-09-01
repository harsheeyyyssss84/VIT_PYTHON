def fibonacci(n):
    """Generate Fibonacci series up to n terms"""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Get input from user
num_terms = int(input("Enter number of terms: "))
fibonacci(num_terms)
