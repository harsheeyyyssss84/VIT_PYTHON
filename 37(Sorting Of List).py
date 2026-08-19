lst = [int(z) for z in input("Enter Numbers Spaced Equally: ").split()]         # IMP LINE(STEP)

print("Default List:", lst)

lst.sort()

print("Sorted:", lst)

lst.sort(reverse="True")

print("Reverse Sorted:", lst)