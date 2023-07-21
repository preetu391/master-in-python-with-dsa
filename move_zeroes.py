def moveZeroes(nums):
    num_of_zeroes = 0
    ans = []
    for ele in nums:
        if ele == 0:
            num_of_zeroes +=1
        else:
            ans.append(ele)
    while num_of_zeroes:
        ans.append(0)
        num_of_zeroes -=1

    return ans

def moveZeroes_inPlace(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j]:
            nums[i] , nums[j] = nums[j] , nums[i]
            i+=1
    return nums

print(moveZeroes_inPlace([0,1,3,0,12]))
    