def minEatingSpeed(piles, h):
    for k in range(1,max(piles)+1):
        hrs = 0
        for pile in piles:
            hrs += pile//k+(pile%k>0)
        if (hrs<=h):
            return k
    return -1

def isFeasible(piles, k, h):
    hrs =0
    for pile in piles:
        hrs += pile//k+(pile%k>0)
        if (hrs>h):
            return False
    return True

def minEatingSpeed_binarySearch(piles, h):
    left, right = 1, max(piles)
    ans = right
    while left<=right:
        mid = (left+right)//2
        if isFeasible(piles, mid, h):
            ans = min(mid, ans)
            right = mid - 1
        else:
            left = mid + 1
    return ans

piles = [3,6,7,11]
h = 8

print(minEatingSpeed_binarySearch(piles, h))
