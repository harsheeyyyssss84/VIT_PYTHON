list1=eval(input("Enter List: "))

num=[]

for i in range (len(list1)):
    if list1[i] == max(list1):
        num.append(list1[i])
        print("MAX Num Is: ", num)

    elif list1[i] != max(list1):
        print("finding...")

    else:
        print("INVALID INPUT")