#dictianry is a mutable data structure that is used to store key value pairs

countries_capitals = {"Australia": "Canberra", "Nepal": "Kathmandu"} #empty dict
countries_capitals2 = {"India":"New Delhi", "France": "Paris"} #creation of dictionary

print(countries_capitals2["India"]) #accessing values related to key
print(countries_capitals.get("Australia"))

for key in countries_capitals2:         #traverse a dict
    print(key, " ", countries_capitals2[key])

countries_capitals2["USA"] = "Washington DC" #add an element to dictionary
countries_capitals2.update(countries_capitals) #add a dict to the end

del countries_capitals["Nepal"] #delete element from dictionary
countries_capitals2.pop("USA")
countries_capitals2.popitem()

print("India" in countries_capitals2) #membership of a key in dict

print(countries_capitals2.keys()) #to access all keys of a dict
print(countries_capitals2.values()) #to access all values of a dict

l1= ["1", "2"]
dictionary = dict.fromkeys(l1,"a")

print(dictionary)

print(countries_capitals)
print(countries_capitals2)