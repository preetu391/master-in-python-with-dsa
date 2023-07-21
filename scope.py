var1 = "hi" #global 

def print_var():
    # var1 = "hello" #local
    print(var1)

def outer():
    var1 = "hello1" 
    def inner():
        var1 = "hi1"
        print(var1)
    inner()
    print()

outer()
print_var()
print(var1)