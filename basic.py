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

s="Welcome to the hotel"
print(s)
print(type(s))
print(s[1])
print(s[-1])

l = [1, 2, 3, "h", "i", 4]
print(l)
print(type(l))
print(l[-2])


