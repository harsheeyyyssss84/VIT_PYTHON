num=int(input("Enter Number: "))

fact=1

for i in range(1,num+1):
    fact*=i
    i+=1

print("Factorial Of", num, "IS: ", fact)