# largest of 3 number without max() function

# def largest(a,b,c):
#     if a >= b and a >= c:
#         return f"{a} is Largest"
        
#     elif b >= a and b >= c:
#         return f"{b} is Largest"
        
#     elif c >= a and c >= b:
#         return f"{c} is Largest"
    
#     else:
#         return "All Are Equal"

# num1 = int(input("Enter Number 1: "))
# num2 = int(input("Enter Number 2: "))
# num3 = int(input("Enter Number 3: "))

# print(largest(num1, num2, num3))


# largest of 3 number using max()


# d = float(input("Enter First Number: "))
# e = float(input("Enter Second Number: "))
# f = float(input("Enter Third Number: "))

# largestt = max(d, e, f)

# print("Largest Number Is: ", largestt)


# sum of n natural number using recursion


# def summ(n):
#     if n < 0:
#         return "Enter Positive Number"
#     elif n == 0:
#         return 0
#     else:
#         return n + summ(n-1)

# print(summ(int(input("Enter Number: "))))


# sum of n Natural Numbers


# n1 = int(input("Enter Number: "))
# sum = 0

# if n1 < 0:
#     print("Enter Positive Number")

# elif n1 == 0:
#     print("0")

# else:
#     for i in range(n1+1):
#         sum+=i
#         i+=1

# print("Sum Of N Natural Numbers Is:", sum)


# Number of Vowels in a String


# string = str(input("Enter String: "))

# vowels = "AEIOUaeiou"

# num2 = 0

# for ch in string:
#     if ch in vowels:
#         num2 += 1

# print("Number Of Vowels In Your Line Is/Are:", num2)


# sorting of a list


lst = [int(z) for z in input("Enter Numbers Spaced Equally: ").split()]

print(lst)

lst.sort()

print("Sorted:", lst)

lst.sort(reverse="True")

print("Reverse Sorted:", lst)