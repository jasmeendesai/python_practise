# Basics of python
# a = input()
# b = input()
# print(f"Sum is {a+b}")

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

num = int(input("Enter your score: "))
if (num > 8):
    y = 9
print(y) 
