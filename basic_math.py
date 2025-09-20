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