# Basics of python
# a = input()
# b = input()
# print(f"Sum is {a+b}")

# tuple -> a = ("a", "b", "c")
# list -> b = ["a", "b", "c"]
# dict -> obj


# Taking Multiple inputs

# x, y = input("Enter two number : ").split()
# print("first number ", x)
# print("second number ", y)

# ---------------------------------------------------

# If else

# WAP to accept the score of a student. Print a congratulatory message if the score is greater than 70.
# score = int(input("Enter the score of student : "))
# if(score > 70):
#     print(f"Congratulation!")

# WAP to print Gold Medal if the score of student is a perfect 100
# new_score = int(input("Enter the score : "))
# if(new_score == 100):
#     print("Gold Medal")

# WAP to accept the score of a student. Print a congratulatory message if the score is greater than 70. If the score is less than or equal to 70, print a relevant message.
# stu_score = int(input("Enter the score : "))
# if(stu_score > 70):
#     print("Congratulations!")
# else:
#     print("Score less than 70 try best!")

"""
WAP to accept an integral input and print the corresponding message based on the given conditions:

Divisible by both 5 and 8 ⇒ Print 58

Divisible by only 5 ⇒ Print 5

Divisible by only 8 ⇒ Print 8

Divisible by neither 5 nor 8 ⇒ Print “None”

x%y ⇒ Remainder when x is divided by y

"""
# num = int(input("Enter the number : "))
# if(num % 5==0 and num%8==0):
#     print(58)
# elif(num%5==0 and num%8 !=0):
#     print(5)
# elif(num%5 !=0 and num%8 == 0):
#     print(8)
# else:
#     print("None")

# num = int(input("Enter your score: "))
# if (num > 8):
#     y = 9
# print(y)

# WAP to find maximum of 3 distinct numbers using Nested If-Else
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))

# if(a>b):
#     if(a>c):
#         print(f"a is greater")
#     else:
#         print(f"c is greater")
# else:
#     if(b>c):
#         print(f"b is greater")
#     else:
#         print(f"c is greater")


# Assignment: WAP to find maximum of 4 distinct numbers using Nested If-Else

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))
# d = int(input("Enter fourth number : "))

# if(a>b):
#     if(a>c):
#         if(a>d):
#             print(f"a greater")
#         else:
#             print(f"d greater")
#     else:
#         if(c>d):
#             print(f"c is greater")
#         else:
#             print(f"d is greater")
# else:
#     if(b>c):
#         if(b>d):
#             print(f"b is greater")
#         else:
#             print(f"d is greater")
#     else:
#         if(c>d):
#             print(f"c greater")
#         else:
#             print(f"d is greater")


# WAP to print relevant message according to the grade of the student.
# grade = int(input("Enter the grade : "))
# match(grade):
#     case 10 :
#         print("Outstanding")
#     case 9 :
#         print("Execellent")
#     case 8 :
#         print("Good")
#     case 7 :
#         print("Average")
#     case default:
#         print("Fail")
    