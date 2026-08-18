text = str(input("Enter String: "))

if text[::-1] == text:
    print("Palindrome")

else:
    print("Not A Palindrome")