print("Hello World")

# BELOW THREE LINES ARE VERY IMPORTANT!!!
# in a function(def function) it is very important to "return"
# the last line with the def indentation
# ex

# def sum(a,b):
#     s=a+b
#     return s          #very important for def functions

# print(sum(2,5))       #calling the function with print statement
# print(sum(34,46))


# def calsum(c,d):
#     sum=c+d
#     print(sum)
#     return sum

# calsum(4,5) 


# def calavg(e,f,g):
#     avg=(e+f+g)/3
#     print(avg)
#     return avg

# calavg(1,2,3)


# recursion example

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)

fact1 = int(input("Enter Number to calculate Factorial: "))
print(fact(fact1))