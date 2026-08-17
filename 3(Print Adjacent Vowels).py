vowel="aeiouAEIOU"

user=eval(input("Enter String: "))

count=0

for i in range(len(user) - 1):
    if user[i] in vowel and user[i+1] in vowel:
        count+=1
        print("Total number of adjacent vowels are: ", count, "And it is: ", user[i]+user[i+1])