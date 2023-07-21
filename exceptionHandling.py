
def func():
    try:
        n = int(input("Enter an integer: "))
        l = [1,2,3,4]
        return 1
    except ValueError: 
        return 0
    except IndexError:
        return 0 
    finally:
        print("hello")

func()
# finally:
#     print("I am finally block")

# print(dir(locals()['__builtins__']))