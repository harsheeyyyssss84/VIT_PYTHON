def calc_sum(n):
    if (n == 0):
        return 0
    else:
        return n + calc_sum(n-1)

sum = calc_sum(int(input("Enter Number: ")))
print(sum)