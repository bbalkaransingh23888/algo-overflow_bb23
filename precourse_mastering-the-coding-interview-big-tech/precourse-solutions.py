### Chapter 1: ARRAYS: EASY - TWO SUM ###

##Section 1: BRUTE FORCE SOLUTION##
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

two_sum([1,3,7,9,2], 11)
two_sum([2], 2)
two_sum([], 1)
two_sum([2,3], 5)
two_sum([1,2,3], 6)