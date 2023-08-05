from threading import *

class print_hello(Thread):
    def run(self):
        for i in range(3):
            print("hello")

class print_hola(Thread):
    def run(self):
        for i in range(3):
            print("hola")

obj1 = print_hello()
obj2 = print_hola()

obj1.start()
obj2.start()

obj1.join()
obj2.join()

print("done")