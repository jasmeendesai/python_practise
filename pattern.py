# https://takeuforward.org/pattern/pattern-1-rectangular-star-pattern/

def rectangularPattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print("")

rectangularPattern(3)

# https://takeuforward.org/pattern/pattern-2-right-angled-triangle-pattern/

def right_angled_triagnle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print("")

right_angled_triagnle(5)

# https://takeuforward.org/pattern/pattern-3-right-angled-number-pyramid/

def right_angled_number_pyramid(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        print()

right_angled_number_pyramid(5)

def right_angled_number_pyramid2(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

right_angled_number_pyramid2(5)

# https://takeuforward.org/pattern/pattern-4-right-angled-number-pyramid-ii/

def right_angled_number_pyramid_ii(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end="")
        print()

right_angled_number_pyramid_ii(5)

# https://takeuforward.org/pattern/pattern-5-inverted-right-pyramid/

def inverted_right_pyramid(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        print()

inverted_right_pyramid(5)

# https: //takeuforward.org/pattern/pattern-6-inverted-numbered-right-pyramid/

def inverted_numbered_right_pyramid(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1, end="")
        print()

inverted_numbered_right_pyramid(5)

# https: //takeuforward.org/pattern/pattern-7-star-pyramid/

def star_pyramid(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        for j in range(n-i-1):
            print(" ", end="")
        print()

star_pyramid(5)


# https: //takeuforward.org/pattern/pattern-8-inverted-star-pyramid/

def inverted_star_pyramid(n):
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(2*n - (2*i+1)):
            print("*", end="")
        for j in range(i):
            print(" ", end="")
        print()

inverted_star_pyramid(5)

# https://takeuforward.org/pattern/pattern-9-diamond-star-pattern/

def diamond_star(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(2*i+1):
            print("*", end="")
        for j in range(n-i-1):
            print(" ", end="")
        print()
    for i in range(n):
        for j in range(i):
            print(" ", end="")
        for j in range(2*n - (2*i+1)):
            print("*", end="")
        for j in range(i):
            print(" ", end="")
        print()

diamond_star(5)


# https://takeuforward.org/pattern/pattern-10-half-diamond-star-pattern/

def half_daimond_star(n):
    for i in range(1, 2*n):
        # first half number of stars equal to number of rows
        stars = i

        # second half number stars decreases by one by increasing rows i,e. stars = (2n-i)
        if(i>n):
            stars = 2*n-i

        for j in range(stars):
            print("*", end="")
        print()

half_daimond_star(5)

# https://takeuforward.org/pattern/pattern-11-binary-number-triangle-pattern/

def binary_num_tri(n):
    for i in range(n):
        start = 1 if i%2==0 else 0

        for j in range(i+1):
            print(start, end="")
            start = 1 - start
        print()

binary_num_tri(5)

# https: //takeuforward.org/pattern/pattern-12-number-crown-pattern/

def number_crown(n):
    spaces = 2 * (n-1)

    for i in range(1, n+1):
        # print number
        for j in range(1, i+1):
            print(j, end="")

        # print spaces
        for j in range(spaces):
            print(" ", end="")

        # print number
        for j in range(i, 0, -1):
            print(j, end="")

        print()
        spaces-=2


number_crown(5)

# https://takeuforward.org/pattern/pattern-13-increasing-number-triangle-pattern/

def incr_num_tri(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            print(num, end="")
            num += 1

        print()

incr_num_tri(5)

# https: //takeuforward.org/pattern/pattern-14-increasing-letter-triangle-pattern/

def letter_tri(n):
    for i in range(n):
        for ch in range(ord('A'), ord('A')+i+1):
            print(chr(ch), end="")
        print()

letter_tri(5)


# https: //takeuforward.org/pattern/pattern-15-reverse-letter-triangle-pattern/

def rev_letter_tri(n):
    for i in range(n):
        for ch in range(ord('A'), ord('A')+(n-i)):
            print(chr(ch), end="")
        print()

rev_letter_tri(5)

# https://takeuforward.org/pattern/pattern-16-alpha-ramp-pattern/

def alpha_ramp(n):
    for i in range(n):
        ch = ord('A') + i
        for j in range(i+1):
            print(chr(ch), end="")
        print()

alpha_ramp(5)

# https://takeuforward.org/pattern/pattern-17-alpha-hill-pattern/

def alpha_hill(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")

        ch = ord('A')
        breakpoint = (2*i+1)//2
        for j in range(2*i+1):
            print(chr(ch), end="")

            if(j<breakpoint):
                ch +=1
            else :
                ch -=1

        for j in range(n-i-1):
            print(" ", end="")

        print()

alpha_hill(5)


# https: //takeuforward.org/pattern/pattern-18-alpha-triangle-pattern/

def alpha_tri(n):
    for i in range(n):
        ch = ord('A')+(n-i-1)
        for j in range(i+1):
            print(chr(ch), end="")
            ch += 1
        print()

alpha_tri(5)

# or

def alpha_tri2(n):
    for i in range(n):
        for ch in range(ord('A')+n-i-1, ord('A')+n):
            print(chr(ch), end="")

        print()

alpha_tri2(5)

# https://takeuforward.org/pattern/pattern-19-symmetric-void-pattern/

def sym_void(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        for j in range(2*i):
            print(" ", end="")
        for j in range(n-i):
            print("*", end="")
        print()
    
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        for j in range(2*n-(2*(i+1))):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

sym_void(5)
    
# https: //takeuforward.org/pattern/pattern-20-symmetric-butterfly-pattern/

def sym_butterfly(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        for j in range(2*n - (2*(i+1))):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

    for i in range(n):
        for j in range(n-i-1):
            print("*", end="")
        for j in range(2*(i+1)):
            print(" ", end="")
        for j in range(n-i-1):
            print("*", end="")
        print()

sym_butterfly(5)


# https: //takeuforward.org/pattern/pattern-21-hollow-rectangle-pattern/

def hollow_rect(n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or i==n-1 or j==n-1):
                print("*", end='')
            else : 
                print(" ", end="")
        print()

hollow_rect(5)
