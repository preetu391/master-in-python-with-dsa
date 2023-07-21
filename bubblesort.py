def bubble_sort(list, n):
    for i in range(0,n-1):
        if_swapped = False
        for j in range(0,n-i-1):
            if(list[j]>list[j+1]):
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
                if_swapped = True
        if(if_swapped==False):
            break

list = []
n = int(input("Please enter the size of the list "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
bubble_sort(list,n)
print("sorted list is: ")
for i in range(0,n):
    print(list[i], end=" ")