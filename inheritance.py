class pet:
    name = ""
    def stays_at(self):
        print("stays at home")

class eat:
   def eats(self):
      print("my pet eats")

class dog (pet,eat):
    def stays_at(self):
       return super().stays_at()
    def info(self):
     print("My dogs name is ",self.name)

class dog_child(dog):
   def tell(self):
      print("I am dog child")

my_dog = dog()
my_dog.name = "Jackie" #attribute of superclass

my_dog.stays_at() #of superclass that is pet

my_dog.info() #of subclass

my_dog.eats()

my_dog_child = dog_child()
my_dog_child.name= "Champ"

my_dog_child.info()
