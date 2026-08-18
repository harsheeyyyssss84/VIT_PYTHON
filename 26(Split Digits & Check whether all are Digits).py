n = input("Enter Numbers: ").split()            #IMP Function split()

if all(i.isdigit() for i in n):            #IMP Line(IF AND FOR STATEMENT IN ONE LINE WITH A FUNCTION)
                                           #REMEMBER!!!
    print("All Are Digits")
else:
    print("All Are Not Digits")