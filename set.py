set1 = {} #empty dictionary
set2 = set() #empty set
# print(type(set2))

set3 = {1,2,3,4,5} #creating a set
print(set3)

for ele in set3: #traversing a set
    print(ele)

set3.add(6) #add an element to set
l1 = [8,9]
set3.update(l1) #add multiple elements to the set
print(set3)

set3.discard(8) #remove element from set
result = set3.pop() #pop deletes from the first element

print(set3, " ",  result)

set4 = {2,3,5,10}

print(set3.symmetric_difference(set4)) #operations on set



