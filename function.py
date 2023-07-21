def printhello():      #function definition
    print("hello")

printhello()
printhello()
printhello()

def add_numbers(*numbers):
    print(type(numbers))
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)


add_numbers(2,3,4,5,6,7,4,8,10,8,4)

def print_country_and_capital (**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key, " ", value)

print_country_and_capital(India="New Delhi", Australia="Canberra", Nepal = "Kathmandu")