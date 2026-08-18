def cal_prime(n):

    if n < 0:
        return "Prime or Composite Numbers are Not Defined For Negative Numbers"

    elif 0 < n < 2:       # less then 2 all numbers are Prime i.e 0 & 1
        return "Prime Number"

    elif n == 2:
        return "Prime Number"

    else:
        for i in range(2, int(n ** 0.5) + 1):       # important step (int(n ** 0.5) + 1) means loop till (sqrt of n) + 1 as if we do till n it will always be composite as n will itself divide n and give a composite number and also after sqrt of that number further there is only the number itself which can completely divide it and give zero as remainder!!!

            if n % i == 0:      # if remainder = 0 it means it is composite number
                return "Composite Number"

            else:
               return "Prime Number"


print(cal_prime(int(input("Enter Number: "))))