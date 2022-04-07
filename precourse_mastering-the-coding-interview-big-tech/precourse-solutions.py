### Preface: Steps to Solving Technical Questions ###
# Question: 

# ex: input => ; output => 


# Step 1: Verify the constraints (think about edgecases) => 
    

# Step 2: Write out test cases => 
#     - Best case: input => ; output => 
    

# Step 3: Figure out a solution without code (pseudocode) =>
#     - input => 
   

# Step 4: Brute Force Solution => Get to a working solution that is able to find
# a solution if one exists and returns a message or something if there is no solution
# available. See precourse-solutions.py Chapter 1: Section 1 for solution

# Step 5: Code explanation => 
#     - explanation: 

# Step 6: Test the code against the edgecases =>
#     - No solution: input => 

# Step 7: Space and Time Complexity =>
#     - How much of the time and space resources will consume relative to the input size,
#     since inputs usually scale ?

# Step 8: Optimize the Solution 
#     - Can the solution be optimized? If one Complexity is significantly better
#     than the other, then the solution can be optimized. 


# Step 9: Repeat Steps 5-7 with Optimized Solution:

### Chapter 1: ARRAYS: EASY - TWO SUM ###

##Section 1: BRUTE FORCE SOLUTION##
from curses.ascii import isalnum
import math


def two_sum(nums, t):
    # p1, or i, compares each number for the length of the array, 
    # which is derived from length - 1 (arrays start at 0, 
    # so len(nums) - 1 starts the count from the beginning)
    for i in range(len(nums) -1):
        # p2, or j, compares each number that comes after i, or the remaining 
        # length of the array. i+1 starts the count at the second element while
        # len(nums) has the count include every number except the element in i 
        # and the prior elements where applicable
        for j in range(i+1, len(nums)):
            # if the target, or t, minus pointer 1, or i, is equal to
            # pointer 2, or j, the solution is i and j.  
            if t - nums[i] == nums[j]:
                print(i, j)
    # If no answer is found, print null
    print("null")

# two_sum([1,3,7,9,2], 11)
# two_sum([2], 2)
# two_sum([], 1)
# two_sum([2,3], 5)
# two_sum([1,2,3], 6)

##Section 2: OPTIMAL SOLUTION##
def two_sum_optimal(nums, t):
    num_dict = {}
    for i in range(len(nums)):
        if t - nums[i] in num_dict:
            print([num_dict[t - nums[i]], i])
        num_dict[nums[i]] = i
    print("null")
#two_sum_optimal([1,3,7,9,2], 11)
#two_sum_optimal([2], 2)
#two_sum_optimal([], 1)
#two_sum_optimal([2,3], 5)
#two_sum_optimal([1,2,3], 6)


### Chapter 2 - ARRAYS: MEDIUM - CONTAINER WITH MOST WATER ###

##Section 1 - BRUTE FORCE SOLUTION##
def container_with_most_water(walls):
   max_area = 0
   for i in range(len(walls)-1):
       for j in range(i+1, len(walls)):
           height = min(walls[i],walls[j])
           width = j-i
           area = height*width
           max_area = max(max_area, area)
   print(max_area)


# container_with_most_water([7,1,2,3,9])
# container_with_most_water([])
# container_with_most_water([7])
# container_with_most_water([6,9,3,4,5,8])

##Section 2 - OPTIMAL SOLUTION##
def container_with_most_water_optimal(walls):
   i = 0
   j = (len(walls)-1)
   max_area = 0
   while i < j:
        height = min(walls[i],walls[j])
        width = j-i
        area = height*width
        max_area = max(max_area, area)
        if walls[i]<=walls[j]:
            i += 1
        else:
            j -= 1
   print(max_area)


# container_with_most_water_optimal([7,1,2,3,9])
# container_with_most_water_optimal([])
# container_with_most_water_optimal([7])
# container_with_most_water_optimal([6,9,3,4,5,8])



### Chapter 3 - ARRAYS: HARD - TRAPPING RAINWATER ###

##Section 1 - BRUTE FORCE SOLUTION##
def trapping_rainwater(heights):
    total_rainwater = 0
    for i in range(len(heights)-1):
        left = i 
        right = i
        max_left = 0 
        max_right = 0
        while left >= 0:
            max_left = max(max_left, heights[left])
            left -= left
        while right <= len(heights):
            max_right = max(max_right, heights[right])
            right += right
        
        current_water = current_water + (min(max_left, max_right) - heights[i])
        if current_water >= 0:
            total_rainwater = current_water + total_rainwater
    print(total_rainwater)
    

# trapping_rainwater([0,1,0,2,1,0,3,1,0,1,2])
# trapping_rainwater([])
# trapping_rainwater([1])
# trapping_rainwater([3,4,3])


        
##Section 2 - OPTIMAL SOLUTION##

### Chapter 4 - STRINGS: EASY - TYPED OUT STRINGS/BACKSPACE STRING COMPARE

##Section 1 - BRUTE FORCE SOLUTION##
def backspace_string_compare(str_s, str_t):
    arr_s = []
    arr_t = []

    for i in str_s: 
        if i == "#" and arr_s != []:
            arr_s.pop()
        else:
            arr_s.append(i)
        
    
    for j in str_t:
        if j == "#" and arr_t != []:
            arr_t.pop()
        else:
            arr_t.append(j)

    if arr_s == arr_t:
        print(True)
    else:
        print(False)

# backspace_string_compare("ab#z","az#z")
# backspace_string_compare("abc#d","acc#c")
# backspace_string_compare("x#y#z#","a#")
# backspace_string_compare("a###b","b")
# backspace_string_compare("Ab#z","ab#z")

##Section 2 - OPTIMAL SOLUTION##


### Chapter 5 - STRINGS: MEDIUM - LONGEST SUBSTRINE WITHOUT REPEATING CHARACTERS ###

##Section 1 - BRUTE FORCE SOLUTION##
def longest_substring_without_repeating_characters(str):
    longest = 0
    
    if len(str) <= 1: 
        longest = print (len(str))

    for i in str:
        length = 0
        j = i
        for j in str:
            chars = {}
            curr_chars = j
            if chars[curr_chars] != chars:
                length += 1
                chars[curr_chars] = True
                longest = max(longest,curr_chars)
            else:
                break
    print(longest)

# longest_substring_without_repeating_characters("abccabb")
# longest_substring_without_repeating_characters("ccccc")
# longest_substring_without_repeating_characters("")
# longest_substring_without_repeating_characters("s")
# longest_substring_without_repeating_characters("abcbda")

 ##Section 2 - OPTIMAL SOLUTION##


 ### CHAPTER 6a - STRINGS: EASY - VALID PALINDROME ###

 ## Section 1 - BRUTE FORCE SOLUTION ##
def valid_palindrome(str):
    str = str.lower().replace("^[a-z0-9]+$", "")
    str_norm = []
    str_rev = []
    for i in str:
        if i.isalnum():
            str_norm.append(i)

    for j in reversed(str):
        if j.isalnum():
            str_rev.append(j)
    
    if str_norm == str_rev:
        print("True")
    else:
        print("False")


# valid_palindrome("aabaa")
# valid_palindrome("aabbaa")
# valid_palindrome("abc")
# valid_palindrome("a")
# valid_palindrome("")
# valid_palindrome("A man, a plan, a canal: Panama")


### Chapter 6b - STRINGS: EASY - VALID PALINDROME ###

## Section 1 - BRUTE FORCE SOLUTION ##
def valid_sub_palindrome(str,i,j):
    while i < j:
        if str[i] != str[j]:
            return False
        i += 1
        j -= 1
    return True


def almost_palindrome(str):
    str = str.lower().replace("^[a-z0-9]+$", "")
    i = 0
    j = len(str)-1
    
    while i<j:
        if str[i] != str[j]:
            return valid_sub_palindrome(str,i+1,j) or valid_sub_palindrome(str,i,j-1)
        i += 1
        j -= 1
    return True


print(almost_palindrome("race a car")) #True
print(almost_palindrome("aba")) #True
print(almost_palindrome("abccdba")) #True
print(almost_palindrome("abcdefdba")) #False
print(almost_palindrome("a")) #True
print(almost_palindrome("")) #True
print(almost_palindrome("ab")) #True