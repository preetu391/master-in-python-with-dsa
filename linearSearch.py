def linear_search(list, target, size):
    for i in range(0,size):
        if(list[i]==target):
            print(f"Element present at {i} index")
            return
    print("Not found")

list = []
n = int(input("Please enter the size of the list "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
target = int(input("Please enter the target value to be found "))

linear_search(list, target, n)