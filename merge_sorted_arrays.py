def MergeArrays(nums1, m, nums2, n):
    ans = []
    i = 0 
    j = 0
    while i<m and j<n:
        if nums1[i] <= nums2[j]:
            ans.append(nums1[i])
            i+=1
        else:
            ans.append(nums2[j])
            j+=1
    while i<m:
        ans.append(nums1[i])
        i+=1
    while j<n:
        ans.append(nums2[j])
        j+=1
    nums1 = ans
    return nums1

def MergeArrays_additional_pointer(nums1, m, nums2, n):
    k = m+n-1
    i = m-1
    j = n-1
    while j >= 0 and i >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -=1
        else:
            nums1[k] = nums2[j]
            j-=1
        k-=1
    while j>=0:
        nums1 [k] = nums2[j]
        j-=1
        k-=1
    print(nums1)

nums1 = [1,2,3,0,0,0]
m=3
nums2 = [2,5,6]
n=3
print(MergeArrays_additional_pointer(nums1, m, nums2, n))