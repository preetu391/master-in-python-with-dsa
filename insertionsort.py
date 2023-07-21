def insertion_sort(list, n):
    if n<=1:
        return
    for i in range(1,n):
        key = list[i]
        j = i-1
        while j>=0 and key<list[j]:
            list[j+1] = list[j]
            j=j-1

        list[j+1] = key

list = []
n = int(input("Please enter the size of the list "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
insertion_sort(list,n)
print("sorted list is: ")
for i in range(0,n):
    print(list[i], end=" ")
