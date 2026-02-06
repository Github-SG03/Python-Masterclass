 #Creating Point class  
class Point:  
    def __init__(self, a, b):  
        self.a = a  
        self.b = b  
  
    def __str__(self):  
        return str.format("({},{})", self.a, self.b)  
  
def insertion_sort(list1, compare_function):  
    for i in range(1, len(list1)):  
        Value = list1[i]  
        Position = i  
  
        while Position > 0 and compare_function(list1[Position - 1], Value):  
            list1[Position] = list1[Position - 1]  
            PositionPosition = Position - 1  
  
        list1[Position] = Value  
  
U = Point(2,3)  
V = Point(4,4)  
X = Point(3,1)  
Y = Point(8,0)  
Z = Point(5,2)  
  
list1 = [U,V,X,Y,Z]  
  
# We sort by the x coordinate, ascending  
insertion_sort(list1, lambda x, y: x.a > y.a)  
  
for point in list1:  
    print(point)  