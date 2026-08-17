# using conditional statements

# x = float(input("Enter x Coordinate: "))
# y = float(input("Enter y Coordinate: "))

# if x > 0 and y > 0:
#     print("First Quadrant")

# elif x < 0 and y < 0:
#     print("Third Quadrant")

# elif x > 0 and y < 0:
#     print("Fourth Quadrant")

# elif x < 0 and y > 0:
#     print("Second Quadrant")

# elif x == 0 and y == 0:
#     print("Coordinates at Origin")

# else:
#     print("INVALID INPUT")


# using def function (important)


def quadrant(w,z):

    if w > 0 and z > 0:
        print("First Quadrant")

    elif w < 0 and z < 0:
        print("Third Quadrant")

    elif w > 0 and z < 0:
        print("Fourth Quadrant")

    elif w < 0 and z > 0:
        print("Second Quadrant")

    elif w == 0 and z == 0:
        print("Coordinates at Origin")

    else:
        print("INVALID INPUT")


print(quadrant(*eval(input("Enter Coordinates in Form of (x,y): "))))