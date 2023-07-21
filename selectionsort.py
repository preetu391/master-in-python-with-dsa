def selection_Sort(list, n):
    for i in range(0,n):
        min_idx = i
        for j in range(i+1, n):
            if list[j]<list[min_idx]:
                min_idx= j
        (list[i], list[min_idx]) = (list[min_idx], list[i])


list = []
n = int(input("Please enter the size of the list "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
selection_Sort(list,n)
print("sorted list is: ")
for i in range(0,n):
    print(list[i], end=" ")