def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i]+nums[j]==target):
                return [i,j]

def twoSumHashing(nums, target):
    hashtable = {}
    for i in range(len(nums)):
        if nums[i] in hashtable:
            return [hashtable[nums[i]],i]
        else:
            hashtable[target-nums[i]]=i

def twoSumTwoPointer(nums, target):
    nums.sort()
    i = 0
    j = len(nums)-1
    while i<j:
        if nums[i]+nums[j] == target:
            return "Yes"
        elif nums[i]+nums[j] < target:
            i = i+1
        else:
            j=j-1
    return "No"

nums = [3,7,5,11]
target = 9

print(twoSumTwoPointer(nums, target))
