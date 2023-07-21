#list is a data structure that holds a sequence of elements

integers = [1,2,3,4,5,6] #creation of list
#1,2,3,4,5,6 these are elements of this list called integers

for value in integers: #iterating over a list
    print(value)

print(integers[2]) #index
print(integers[-3]) #negative index

print(integers[-4::2]) #slicing

integers.append(7) #append method adds an element to the end of the list
integer2 = [8,9]
integers.extend(integer2) #extend method to add a list to the end of another list
integers.insert(3,0) #insert method to insert at a desirable index in a list

integers[5]=10 #list is a mutable data structure and thus we can change values or list

del integers[5] #delete statement
integers.remove(6) #remove method removes an element from the list
integers.pop() #pop method by default removes an element from last index
integers.pop(1) #pop method takes index as parameter

integers.append(4)
print(integers.count(4)) #count method returns number of occurences of a element in a list

integers.reverse()

# integers.sort(reverse=True)
print(sorted(integers))

print(integers)
