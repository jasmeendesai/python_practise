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


"""
Given the integer day denoting the day number, print on the screen which day of the week it is. Week starts from Monday and for values greater than 7 or less than 1, print Invalid.

Ensure only the 1st letter of the answer is capitalised.

For printing use:-
for Python : print()

"""

def dayOfWeek(day):
    match(day):
        case 1 : print("MONDAY")
        case 2 : print("TUESDAY")
        case 3 : print("WEDNESDAY")
        case 4 : print("THURSDAY")
        case 5 : print("FRIDAY")
        case 6 : print("SATURDAY")
        case 7 : print("SUNDAY")
        case default : print("Invalid")

dayOfWeek(1)
dayOfWeek(0)
dayOfWeek(8)

"""
Loops ---> 
1)while loop --> used to execute a block of statement repeatedly until a give condition is true, when the condition false line after loop executes immediately

------> while with else statement
while condition:
     # execute these statements
else:
     # execute these statements
"""

"""
2) For loop ---> Used for sequential traversal(string, list, tuple, dict, set, ranges) --> In python we have for in loop similar to forEach loop in other languages

-----> Syntax
for iterator_var in sequence:
    statements(s)

------> range() function ---> is commonly used for loops to generate sequence of numbers
--> range(stop) --> generate numbers from 0 till stop --> range(1) --> 0 to 1
--> range(start, stop) --> generate numbers from start to stop --> range(2, 5) ---> 2 to 5 --> 2, 3, 4
--> range(start, stop, step) ---> generate numbers from start to stop incrementing in steps ---> range(0, 10, 2) --> 0, 2, 4, 6, 8


--------->Control Statements
i) continue --> skips the particular iteration
ii) break --> breaks the loop
iii) pass --> used to write empty loops --> it is used for empty control statements, functions, and classes ---> null operator or a placeholder.  It is used when a statement is syntactically required but we don't want to execute any code.

------> enumerate() function --> used with for loop to iterate over the iterable while also keeping track of index of each item
"""
li = [1, 2, 3, 4, 5]
for num in li:
    print(num)

tup = ("geeks", "for", "geeks")
for str in tup:
    print(str)

s = "Geeks"
for i in s:
    print(i)

d = dict({"name" : "Jasmeen", "age" : 27})
for i in d:
    print((i, d[i]))

set1 = {1, 2, 3, 4, 5}
for i in set1:
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5):
    if(i == 3):
        pass
    else:
        print(i)

li = ["eat", "sleep", "repeat"]

for i, j in enumerate(li):
    print(i, j)


"""
Functions --->

syntax --> 
1) def function_name(parameters):
     #statement
     return epxression

2) def function_name(parameter : data_type) -> return_type:
     #statement
     return expression
"""

def evenOdd(x : int) ->str:
    if(x %2 ==0):
        print("Even")
    else:
        print("Odd")

evenOdd(16)
evenOdd(15)