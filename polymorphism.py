class dog:
    def speak(self):
        print("Bark")

class cat:
    def speak(self):
        print("meow")

cat1 = cat()
dog1 = dog()

for animal in (cat1,dog1):
    animal.speak()