# USING STATIC METHOD!!!

# We don't need "self" for Static Methods!!!

class Student:
    @staticmethod       # decorator(Most IMP step to Create Static Methods!!!)
    def college():      # we don't need self here in brackets if we use static method!!!
        print("Vellore Institue of Technology, Chennai")

s = Student()       # to call a class we need to equal it to a variable first then that variable.the function we made in def function!!!
s.college()