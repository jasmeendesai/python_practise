# https: //takeuforward.org/plus/dsa/problems/count-all-digits-of-a-number

"""
Input: n = 4
Output: 1
Explanation: There is only 1 digit in 4.

Input: n = 14
Output: 2
Explanation: There are 2 digits in 14.
"""

# TC -- log(n)+1

def count_dig_num(n):
    # initialise the counter to count the digit
    count = 0 

    # run the loop until n becomes zero
    while(n>0): 
        count +=1

        # divide the number so that last digit is removed as it is already counted
        n = n//10

    return count

print(count_dig_num(4))
print(count_dig_num(14))
print(count_dig_num(653476238432713181))


# TC --> O(1)

import math

def count_dig(n):
    count = int(math.log10(n))+1
    return count

print(count_dig(7789))

"""
 * https://leetcode.com/problems/reverse-integer/description/
 * Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
"""

# TC -- O(log(n))

def rev_num(n):
    rev = 0

    temp = n

    if(temp < 0) :
        x = x * (-1)

    while(n>0):
        ld = n % 10
        rev = rev * 10 + ld
        n = n//10

    if(rev > math.pow(2, 31)-1 or rev < -math.pow(2, 31)):
        return 0
    
    if(temp<0):
        return -rev

    return rev

print(rev_num(7789))


"""
https://leetcode.com/problems/palindrome-number/description/

 Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:
-231 <= x <= 231 - 1
"""

# TC - log(n)

def check_palindrome(n):
    rev = 0
    if(n<0):
        return False
    temp = n
    while(n>0):
        ld = n%10
        rev = rev*10 + ld
        n = n//10

    if(rev > math.pow(2, 31)-1 or rev < -math.pow(2, 31)): 
        return False
    if(temp == rev):
        return True
    else:
        return False
    
print(check_palindrome(121))
print(check_palindrome(-121))


"""
 * https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/
 * Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.
 
An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

 Example 1:
 Input:N = 153
 Output:True
 Explanation: 1^3+5^3+3^3 = 1 + 125 + 27 = 153
                                        
 Example 2:
 Input:N = 371                             
 Output: True              
 Explanation: 3^3+5^3+1^3 = 27 + 343 + 1 = 371
"""

# TC -- O(logn)

def check_amstrongNum(n):
    sum = 0
    temp = n

    k = len(str(n))

    while(n>0):
        ld = n % 10
        sum = sum + (ld ** k)
        n = n//10

    if(temp == sum):
        return True
    else:
        return False
    
print(f"Amstrong number", check_amstrongNum(153))
print(f"Amstrong number", check_amstrongNum(15))

"""
https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/
Problem Statement: Given an integer N, return all divisors of N.
A divisor of an integer N is a positive integer that divides N without leaving a remainder. In other words, if N is divisible by another integer without any remainder, then that integer is considered a divisor of N.

 Example 1:
 Input:N = 36              
 Output:[1, 2, 3, 4, 6, 9, 12, 18, 36]
 Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
         
 Example 2:
 Input:N =12 
 Output: [1, 2, 3, 4, 6, 12]
 Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12. 
"""

# TC -- O(n)

def print_allDivisors(n):
    res = []

    for i in range(1, n+1):
        if(n % i == 0):
            res.append(i)
    return res

print(print_allDivisors(36))

# TC -- 

def print_allDivisors1(n):
    res = []
    limit = int(math.sqrt(n))

    for i in range(1, limit+1):
        if(n % i == 0):
            res.append(i)
            if(i!=n//i):
                res.append(n//i)

    res.sort()
    return res

print(print_allDivisors1(36))


"""
 * https://takeuforward.org/data-structure/check-if-a-number-is-prime-or-not/
 * Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.
 * Example 1:
   Input:N = 2
   Output:True      
   Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).   

   Example 2:   
   Input:N =1         
   Output: False      
   Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.
"""
# TC -- O(n)

def isPrime(n):
    count = 0
    for i in range(1,n+1):
        if(n%i==0):
            count+=1

    if(count == 2): 
        return True
    else:
        return False
    
print(f"Prime", isPrime(11))
print(f"Prime", isPrime(4))

# TC --> O(sqrt(n))

def isPrime2(n):
    count = 0
    limit = int(math.sqrt(n))
    for i in range(1, limit+1):
        if(n%i == 0):
            count +=1
            if(n%i != i):
                count +=1
    
    if(count == 2):
        return True
    else:
        return False
    
print(f"Prime", isPrime2(11))
print(f"Prime", isPrime2(4))


"""
https://takeuforward.org/data-structure/find-gcd-of-two-numbers/
Problem Statement: Given two integers N1 and N2, find their greatest common divisor.
The Greatest Common Divisor of any two integers is the largest number that divides both integers.

Example 1:
Input:N1 = 9, N2 = 12
Output:3
Explanation:Factors of 9: 1, 3 and 9
Factors of 12: 1, 2, 3, 4, 6, 12
Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.

Example 2:
Input:N1 = 20, N2 = 15
Output: 5
Explanation:Factors of 20: 1, 2, 4, 5
Factors of 15: 1, 3, 5
Common Factors: 1, 5 out of which 5 is the greatest hence it is the GCD.
"""
# TC --> O(min(n1, n2))

def gcd_of_two_num(n1, n2):
    gcd = 1
    for i in range(1, min(n1, n2)+1):
        if(n1%i ==0 and n2%i == 0):
            gcd = i

    return gcd


print(f"gcd", gcd_of_two_num(11, 13))
print(f"gcd", gcd_of_two_num(40, 20))

# TC --> O(min(n1, n2)) --> lesser number of iterations

def gcd_nums(n1, n2):
    for i in range(min(n1, n2), 0, -1):
        if(n1%i == 0 and n2%i == 0):
            return i
        
    return 1

print(f"gcd", gcd_nums(11, 13))
print(f"gcd", gcd_nums(20, 40))

# TC --> O(log(a)(min(n1, n2))) --> lesser iterations as compared to both logics --> almost const time

def gcd_nums1(n1, n2):
    while(n1>0 and n2>0):
        if(n1>n2):
            n1 = n1%n2
        else:
            n2 = n2%n1

    if(n1 == 0):
        return n2
    else:
        return n1
    
print(f"gcd", gcd_nums1(11, 13))
print(f"gcd", gcd_nums1(40, 20))
