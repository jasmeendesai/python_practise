"""
Recursion --->
It is a phenomenon when a function calls itself indefinitely until a specified condition is fulfilled.
"""

"""
https://takeuforward.org/recursion/introduction-to-recursion-understand-recursion-by-printing-something-n-times/
"""

"""
 * https://takeuforward.org/recursion/print-name-n-times-using-recursion/
 * 
 * Problem: Print your Name N times using recursion
"""
# TC ---> O(n)
# SC ---> O(n)

def printName(i, n):
    if(i>n): return

    print("Jasmeen")
    printName(i+1, n)

printName(1, 5)

"""
https://takeuforward.org/recursion/print-1-to-n-using-recursion/
 * Problem: Print from 1 to N using Recursion
"""

# M1 --> TC --> O(n)

n = 5

def print1toN(i, n):
    if(i>n) : return
    print(i)
    print1toN(i+1, n)

print1toN(1, n)

# M2 --> TC --> O(n) | SC --> O(n)

def print1toN1(i):
    if(i<1) : return
    print1toN1(i-1)
    print(i)

print1toN1(n)


"""
* https://takeuforward.org/recursion/print-n-to-1-using-recursion/
 * Problem: Print from N to 1 using Recursion
"""

# M1 --> TC ==> O(n)

def printNto1(i, n):
    if(i<=0): return
    print(i)
    printNto1(i-1, n)

printNto1(n, n)

# M2 --> TC --> O(n) | SC --> O(n)

def printNto11(i, n):
    if(i>n) : return
    printNto11(i+1, n)
    print(i)

printNto11(1, n)

"""
https://takeuforward.org/data-structure/sum-of-first-n-natural-numbers/
Sum of first N Natural Numbers ===> Problem statement: Given a number ‘N’, find out the sum of the first N natural numbers.

Example 1:
Input: N=5
Output: 15
Explanation: 1+2+3+4+5=15

Example 2:
Input: N=6
Output: 21
Explanation: 1+2+3+4+5+6=21
"""

# M1 --> Parameterized way
"""
In this approach, instead of using a global variable for calculating the sum, we pass the sum in the parameters of the function each time we add an integer to it during the function call. The sum gets incremented by an ith integer and i get decremented by 1 in each function call. At the end when i becomes less than 1, we simply return the calculated sum until that point. 

To understand this parameterized approach better, let us have a look at the pseudocode given below:

void func(i,sum)
{
   if(i<1)
   {
     print(sum);
     return;
   }

func(i-1,sum+i);

}

main()
{
   input(n);
   func(n,0);

}
"""

def print_sum_n_natural_num(i, sum) :
    if(i<1) :
        print(sum)
        return
    print_sum_n_natural_num(i-1, sum+i)

print_sum_n_natural_num(n, 0)

# M2 ---> Functional Way

"""
This approach is a lot simpler than the parameterized recursion. We can visualize the sum of n natural numbers in the following way as shown below:

sumOfNaturalNumbers(N) = N + sumOfNaturalNumbers(N-1);
The Sum of N natural numbers would just be the Nth integer added to the Sum of (N-1) natural numbers. The base case can be visualized as if n decreases to 0, then we return 0 because the sum of 0 natural numbers is 0 only. Here, we’ve just broken the problem into 2 subparts and the answers of both these subparts would be added and stored in the Sum(n) function which would then be printed at last.

To understand this functional approach better, let us have a look at the pseudocode given below:

int func(n)
{
   if(n == 0)
   {
     return 0;
   }

return n + func(n-1);

}

main()
{
   input(n);
   func(n);

}
"""

def print_sum_n_natural1(n):
    if(n == 0):
        return 0
    
    return n + print_sum_n_natural1(n-1)

print(print_sum_n_natural1(n))

"""
https://takeuforward.org/data-structure/factorial-of-a-number-iterative-and-recursive/
Factorial of a Number : Iterative and Recursive ==> Problem Statement: Given a number X,  print its factorial.

To obtain the factorial of a number, it has to be multiplied by all the whole numbers preceding it. More precisely X! = X*(X-1)*(X-2) … 1.

Note: X  is always a positive number. 
Example 1:
Input: X = 5
Output: 120
Explanation: 5! = 5*4*3*2*1

Example 2:
Input: X = 3
Output: 6
Explanation: 3!=3*2*1
"""

# M1 ==> Parameterized way

def factorial_of_n(i, fact):
    if(i <= 1):
        print(fact)
        return
    factorial_of_n(i-1, fact*i)

factorial_of_n(n, 1)

# Functional way

def factorial_of_n1(i):
    if(i <= 1):
        return 1
    return i*factorial_of_n1(i-1)

print(factorial_of_n1(n))


"""
 * https://takeuforward.org/data-structure/reverse-a-given-array/
 * Reverse a given Array
Practice:
Solve Problem
Problem Statement: You are given an array. The task is to reverse the array and print it. 

Example 1:
Input: N = 5, arr[] = {5,4,3,2,1}
Output: {1,2,3,4,5}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.

Example 2:
Input: N=6 arr[] = {10,20,30,40}
Output: {40,30,20,10}
Explanation: Since the order of elements gets reversed the first element will occupy the fifth position, the second element occupies the fourth position and so on.
"""

arr = [5, 4, 3, 2, 1]
N = 5


def reverseArr(arr, left, right):
    if (left >= right):
        return

    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

    reverseArr(arr, left+1, right-1)


reverseArr(arr, 0, N-1)
print(arr)

arr1 = [5, 4, 3, 2, 1]


def reverseArr1(arr, i):
    n = len(arr)

    if (i >= n/2):
        return

    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1] = temp

    reverseArr1(arr, i+1)


reverseArr1(arr1, 0)
print(arr1)

"""
https://leetcode.com/problems/valid-palindrome/
. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

# s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = " "

def isPalindrome(s):
    cleaned = ''
    for char in s:
        if(char.isalnum()):
            cleaned += char.lower()

    return helper(cleaned, 0)

def helper(s, i):
    n = len(s)
    if(i>=n/2):
        return True
    
    if(s[i] != s[n-i-1]): return False

    return helper(s, i+1)

print(isPalindrome(s))


"""
 * https://leetcode.com/problems/fibonacci-number/
 * 
 * Fibonacci Number
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Constraints:

0 <= n <= 30
"""
# num = 2
# num = 3
num = 4

def fib(n):
    if(n<=1): return n

    last = fib(n-1)
    secLast = fib(n-2)

    return last+secLast

print(fib(num))