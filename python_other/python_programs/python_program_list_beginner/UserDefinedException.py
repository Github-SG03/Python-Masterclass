class EmptyError( RuntimeError ):  
   def __init__(self, argument):  
      self.arguments = argument  
#Once the preceding class has been created, the following is how to raise an exception:  Code  
var = " "  
try:  
    raise EmptyError( "The variable is empty" )  
except (EmptyError, var):  
    print( var.arguments )  