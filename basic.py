"""
Complete the function printNumber which takes an integer input from the user and prints it on the screen.
Use:-
for Python : print()

"""
# m1
def printNumber():
    num = int(input())
    print(num)

# printNumber()


# m2
class Solution:
    def printNumber1(self):
        num = int(input())
        print(num)

sol = Solution()
# sol.printNumber1()

"""
Data types in python -->

1) Numeric type --> int, float, complex
2) Sequence Type --> string, list, tuple
3) Boolean --> bool
4) Mapping Type --> dict
5) Set Type --> set

"""

"""
Numeric Type ------->

1) int ---> represented by class int --> contains +ve/-ve whole number without decimal --> in python no limit how long integer value can be 
2) float ---> represented by class float --> contains decimal point --> Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
3) complex ---> reperesented by class complex --> it is specified as (real)+(imag)j 
"""

a = 5
print(type(a))

b = 5.6
print(type(b))

c = 7+8j
print(type(c))


"""
Sequence Type ---------->

1)string --> string data type
2)list --> like array in other languages -- ordered collection of similar or different data
3)tuple --> similar to list only difference is tuples are immutable
"""
# String
s="Welcome to the hotel"
print(s)
print(type(s))
print(s[1])
print(s[-1])

# List
l = [1, 2, 3, "h", "i", 4]
print(l)
print(type(l))
print(l[-2])
l.append(5) 
print(l)
l.remove(3)
print(l)

# Tuple
tup1 = ()
tup2 = ('geek', 'hi')

print(tup2)
print(type(tup2))

tup = tuple([1, 2, 3, 4, 5])
print(tup)


"""
Boolean Type ------------>
True / False valuse --> python is case sensitive 
Belongs to class bool
"""
print(type(True))
print(type(False))


"""
Set Type ---------------->
set is unorderd collection of data types that is iterable, mutable and has no duplicate
"""

s1 = set("GeeksforGeeks")
print(s1)

s2 = set(["Geeks", "for", "Geeks"])
print(s2)

# loop through set
for i in s1:
    print(i)

print("Geeks" in s2)


"""
Dictionary Type ---------->
it is collection of data values that is used to store data values like a map ---- in the form of key : value pair

values can be of any datatype and be duplicated. but keys are unique and immutable
"""

d1 = {"name" : "Jasmeen", "age" : 27}
print(d1)
print(type(d1))

d2 = dict({"name" : "Jasmeen", "age" : 27})
print(d2)

print(d2["name"])
print(d2.get("name"))

"""
Given marks of a student, print on the screen:

Grade A if marks >= 90
Grade B if marks >= 70
Grade C if marks >= 50
Grade D if marks >= 35
Fail, otherwise.
"""
def studentGrade(marks):
    if(marks >=90):
        print("Grade A")
    elif(marks >=70):
        print("Grade B")
    elif(marks >=50):
        print("Grade C")
    elif(marks >=35):
        print("Grade D")
    else:
        print("Grade Fail")

studentGrade(70)


class Solution:
    def studentGrade(marks):
        if(marks >=90):
            print("Grade A")
        elif(marks >=70):
            print("Grade B")
        elif(marks >=50):
            print("Grade C")
        elif(marks >=35):
            print("Grade D")
        else:
            print("Grade Fail")


Solution.studentGrade(95)


class Solution:
    def studentGrade(self, marks):
        if (marks >= 90):
            print("Grade A")
        elif (marks >= 70):
            print("Grade B")
        elif (marks >= 50):
            print("Grade C")
        elif (marks >= 35):
            print("Grade D")
        else:
            print("Grade Fail")

grade = Solution()
grade.studentGrade(30)
