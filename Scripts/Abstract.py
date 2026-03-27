#Abstract Base Class
from abc import ABC,abstractmethod
class Shape(ABC):
  """Abstract base class for all shapes."""

  @abstractmethod
  def area(self):
    """Abstract method to calculate the area of the shape."""
       #pass  :it is not allowed as abstract method definition without @abstractmethod
  @abstractmethod
  def perimeter(self):
    """Abstract method to calculate the perimeter of the shape."""
      #pass  :it is not allowed as abstract method definition  without @abstractmethod
  def display(self):
      print("hi i'm calling from 'Shape' Abstarct Base class:")
       

