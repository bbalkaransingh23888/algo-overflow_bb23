### Chapter 1: ARRAYS: EASY - TWO SUM ###

##Section 1: BRUTE FORCE SOLUTION##
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
