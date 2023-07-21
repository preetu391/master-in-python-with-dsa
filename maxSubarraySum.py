import math
def max_sum(nums):
    maxValue = - math.inf
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum+=nums[i]
        maxValue = max(curr_sum, maxValue)
        if(curr_sum<0):
            curr_sum = 0
    return maxValue

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_sum(nums))