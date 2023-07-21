var1 = 12
var4 = 1.25
var5 = "hello"

print("this is var1 its value is %d and we have a float value with %f and we have a string that says %s"%(var1, var4,var5))

print("interpolation using format method")

print("{} is an integer, {} is a float value".format(var1, var4))

print("f-strings")

var2 = f"{var1} is an integer, {var4} is a float value"

print(var2)