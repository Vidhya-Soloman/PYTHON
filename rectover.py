#USING FUNCTION FOR DIFFERENT FORMS
class Rectangle:
 def __init__(self,length,width):
  self.__length=length
  self.__width=width
 def area(self):
  area=self.__length*self.__width
  return area
 def __lt__(self,other):
  return self.area()<other.area()
rect1=Rectangle(2,3)
rect2=Rectangle(3,9)
print("area of rect 1",rect1.area())
print("area of rect 2",rect2.area())


#OPERATORS ARE USED FOR MANY THINGS 
#TO COMPARE TO OBJECTS OPERATOR OVERLOADING IS REQUIRED
#WITHOUT USING OPERATOR OVERLOADING METHODS(__ADD__,__LT__) OBJECTS CANNOT BE COMPARED

if (rect1<rect2):
 print("rect 2 is greater")
else:
 print("rect 1 is greater")
