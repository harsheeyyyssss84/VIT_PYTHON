# NON STATIC METHODS!!!


# class Car:
#     color = "blue"
#     brand = "mercbenz"

# car1 = Car()        # made a object (car1) in "class Car" OOPS (VERY IMPORTANT STEP!!!)

# print(car1.color)
# print(car1.brand)


# # construction (__init__ function)


# class Student:

#     # default constructors

#     def __init__(self):
#         pass

#     # parameterized constructors
    
#     def __init__(self, name, marks, gender):        # here self is just a parameter or reference it can be anything ex. abcd e.t.c!!!
#         self.name = name
#         self.marks = marks
#         self.gender = gender
#         print("Adding new student in Database...")

# s1 = Student("karan", 97, "M")
# print(s1.name, s1.marks, s1.gender)

# s2 = Student("astha", 34, "F")
# print(s2.name, s2.marks, s2.gender)

# s3 = Student("aryan", 100, "M")
# print(s3.name, s3.marks, s3.gender)




# # VERY IMPORTANT ONE!!!!!

# # Create students class that takes name & marks of 3 subjects as argument in constructor.
# # Then create a method to print the average!!!
# # MY VERSION


# class Students:

#     def __init__(self, name, sub1, sub2, sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
#         print("Taking Inputs & Analyzing...")


# name = input("Enter Name of Student: ")
# sub1 = float(input("Enter Marks of Student of First Subject: "))
# sub2 = float(input("Enter Marks of Student of Second Subject : "))
# sub3 = float(input("Enter Marks of Student of Third Subject: "))


# p1 = Students(name, sub1, sub2, sub3)


# print("Name:",p1.name)
# print("Marks of Subject 1:",p1.sub1)
# print("Marks of Subject 2:",p1.sub2)
# print("Marks of Subject 3:",p1.sub3)

# avg = (p1.sub1 + p1.sub2 + p1.sub3)/3


# print("Average =", avg)


# MAM VERSION(VVVIMP!!!)
# VERY VERY IMPORTANT [REMEMBER!!!] !!!


class Bacche:

    def __init__(self, namee, markss):
        self.namee = namee
        self.markss = markss

    def cal_avg(self):
        sum = 0
        for val in self.markss:         # jab self use karte hai toh sirf marks se kaam nhi chalta!!!
                                        # self.marks karna padhta hai!!!
            sum+=val
        print("Hello LODU", self.namee, "your Average Score Is: ", sum/5)


namee = input("Enter Name: ")
markss = []

for i in range(0,5,1):
    mark = float(input(f"Enter Marks of Subject {i+1}: "))
    markss.append(mark)


z1 = Bacche(namee, markss)
z1.cal_avg()