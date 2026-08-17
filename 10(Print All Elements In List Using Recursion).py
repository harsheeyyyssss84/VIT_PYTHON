# print all elements in a list using recursion!!!


def print_list(list, idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "apple", "banana", "grapes", "kiwi"]

print_list(fruits, 0)



# print all elements in a list using loops!



# lst = eval(input("Enter List: "))
# if len(lst) == 0:
#         print("List is Empty!")
# else:
#     for i in range(0, len(lst)):
#         print(lst[i])
#     i+=1