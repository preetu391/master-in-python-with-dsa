from abc import ABC

class polygon(ABC): #abstract class
   def sides(self):
      pass
   
class Square(polygon):
   def sides(self):
      print("4 sides")

class Triangle(polygon):
   def sides(self):
      print("3 sides")

obj1 = Square()
obj2 = Triangle()

obj1.sides()
obj2.sides()
