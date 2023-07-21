string = 'abc@123'
string2 = "abc"

print(string, " ", string2)

string3 = '''hi
welcome
to
geekcoders'''

print(string3)

l = [1,"hello", (1,2,3), {"name": "geekcoders"}]

for ele in l:
    print(type(ele), end=" ")

for ele in string:
    print(type(ele), end=" ")

string = "$dsghdvsg"

for i in range(0,len(string)):
    print(string[i], end= " ")

print(string[4::])

print("@" in string)

string5 = "hi friends, how are you"

print(string5.capitalize())

string6 = "gHJHGfhdsgHH123$"

print(string6.lower(), " ", string6.upper())

print(string5.title())

string7 = "hello hi hello hi hello"

print(string7.count("hello",0,10))

print(string7.find("g"))

print(string7.replace("hi", "hii", 1))

print(string6.swapcase())

t = {"hello":1, "abc":2, "123":3}
string8 = "#".join(t)

print(string8)



