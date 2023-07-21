def binary_search(list, target, size):
    l = 0
    r = size - 1
    mid = 0
    while l <= r:
        mid = (l+r)//2
        if list[mid] < target:
            l = mid+1
        elif list[mid] > target:
            r = mid-1
        else:
            print(f"element found at {mid} index")
            return
    print("not found")

list = []
n = int(input("Please enter the size of the list "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
target = int(input("Please enter the target value to be found "))

binary_search(list, target, n)