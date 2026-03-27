######################################################OOPS IN PYTHON#######################################################################################
#Example_1.0:creating an empty class in pythonPython3 program to demonstrate defining a class
class Dogs:
	pass


#######################################################PYTHON SETTER  & GETTER METHOD(BEST EXAMPLE OF INSTANCE METHOD)#######################################################################################################
#Example2.0:Python Setter & Getter Method[If we do not want to set the values of instance variable during object creation(by not using constructor) then we can initialize the instance variable after the object creation using 'getter' & setter method]/default constructor will be available
class StudentSetterGetter:
    def setNames(self,name):
        self.name=name
    def getNames(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

def _demo_student_setter_getter():
    try:
        n = int(input("Enter the number of students:"))
    except EOFError:
        return

    student_records=[]#list to store student objects
    for i in range(n):
        s=StudentSetterGetter()
        name=input("Enter the name of student:")
        marks=int(input("Enter the marks of student:"))
        s.setNames(name)
        s.setMarks(marks)
        student_records.append(s)
    for s in student_records:
        print("hello",s.getNames())
        print("your marks are",s.getMarks())
        print()


_demo_student_setter_getter()
    
###########################################################CONSTRUCTOR IN PYTHON############################################################################################
#NOTE:CONSTRUCTOR OVERLOADING IS NOT POSSIBLE IN PYTHON
#Example3.0:Let's have a look at another scenario, what happen if we declare the two same constructors in the class.[####More than One Constructor in Single class]
class StudentConstructorDemo: 
    def __init__(self):  
        print("The second contructor")   #only this constructor will be executed
st = StudentConstructorDemo() #prints "The second contructor"
st.__init__()  #prints "The second contructor"



#Example_3.1:Python Constructor[Creating a class and object with class and instance attribute]
class Employees: 
  company_name='TCS' #creating a class variable can be changed only by class_name but can be accessed by objects_name
  def __init__(self, name, id):  #pyhon constructor
    self.id = id  # creating a instance variable's inside the constructor and using by 'self'
    self.name = name  # creating a instance variable's inside the constructor and using by 'self'
  def display(self):  #instance method
    print("ID:",self.id,"Name:",self.name,"comapny_name:",self.company_name) 
    self.age=23# creating instance variable inside the instance method by using 'self'
    #del self.id 
emp1 = Employees("John", 101)  
emp2 = Employees("David", 102)    
# creating instance variable outside the class and using by object name(reference name)/accessing the instance vaiable
emp1.name ='rocky'   
# accessing display() method to print employee 1 information    
emp1.display()    
# accessing display() method to print employee 2 information  
emp2.display() 
# deleting the instance variables(name) of Employee 
#del emp1.name
# deleting the instance variable(name) of emp2 of Employee by deleting whole class
#del emp2




#Example_3.2:Python Constructor[Creating a class and object with class and instance attribute]
class Dog:
    #class attribute(static variable)
    attr1 = "living_beings"
	#constructor(uses/create/access instance variable)              
    def __init__(self, name):
        self.name = name   # (instance variable)
    #instance method(uses/create/access instance variabme)
    def m1(self):
        self.breed="pomerian"
        self.name="rhony"
        print("name & breed for new dog member is:",self.name,self.breed)
    #class method(uses/create/access static variable)
    @classmethod
    def m2(cls):  #for every class one special object is created by PVM to maintain class level info which is nothing but class level object.here 'cls' is refernce variable to that class object.
        cls.attr2="mammal"
        cls.attr1="aquatic_living_being"
        print("attr_1 & attr_2 of new member is:",cls.attr1,cls.attr2)
        print(id(cls))
    #static metod(uses/create/access static variable)
    @staticmethod #general method(not using any static variable & instance variable)
    def m3():
        pass
# Driver code Object instantiation
print(id(Dog))  #same as print(id(cls))
Rodger = Dog("Rodger")#Dog(Rodger,"Rodger")
Tommy = Dog("Tommy")#Dog(Tommy,"Tommy")
johny=Dog("johny")
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))
# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))
# Accessing the class property
print(Dog.__dict__)# here 'dict' is built-in method
#Accessing the object property(object may have own property)
print(Rodger.__dict__)# here 'dict' is built-in method
#calling m1
johny.m1()
johny.m2()
johny.m3()
#Deleting the class attribute
#del Dog.attr1
#Deleting the whole class
#del Dog

#########################################################TYPES OF CONSTRUCTOR IN PYTHON##########################################################################################################################################
#4.0: Non-Parameterized Constructor[The non-parameterized constructor uses when we do not want to manipulate the value or the constructor that has only self as an argument. Consider the following example.]
class StudentNonParameterized:  
# Constructor - non parameterized  
    def __init__(self):  #non-parameterised
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)  
student_non_param = StudentNonParameterized()  
student_non_param.show("John")

#4.1: Parameterized Constructor[The parameterized constructor has multiple parameters along with the self. Consider the following example.]
class StudentParameterized:  
   #Constructor - parameterized  
   def __init__(self, name):  #parameterised 
    print("This is parametrized constructor")  
    self.name = name  
   def show(self):  
    print("Hello",self.name)  
student_param = StudentParameterized("John") 
student_param.show()  

#4.2: Default Constructor[When we do not include the constructor in the class or forget to declare it, then that becomes the default constructor. It does not perform any task but initializes the objects. Consider the following example.]
class StudentDefaultConstructor:  
    roll_num = 101    #default
    name = "Joseph"
    def display(self):
        print(self.roll_num,self.name)  
student_default = StudentDefaultConstructor()  
student_default.display() 


##############################################################PYTHON BUILT-IN FUNCTION#########################################################################################################################################################################################
#Example5.0:
class StudentBuiltinFunctionDemo:  
    def __init__(self, name, id, age):  #here name,id age is local variable (local to __init__)
        self.name = name  
        self.id = id  
        self.age = age  
# creates the object of the class Student  
student_builtin = StudentBuiltinFunctionDemo("John", 101, 22)  
# prints the attribute name of the object s  
print(getattr(student_builtin, 'name'))  
# reset the value of attribute age to 23  
setattr(student_builtin, "age", 23)  
# prints the modified value of age  
print(getattr(student_builtin, 'age'))  
# prints true if the student contains the attribute with name id  
print(hasattr(student_builtin, 'id'))  
# deletes the attribute age  
delattr(student_builtin, 'age')  
# this will give an error since the attribute age has been deleted  
#print(s.age)  
##############################################################PYTHON BUILT-IN ATTRIBUTES##############################################################################################################################################################################################################################
#Example6.0:
class StudentBuiltinAttributesDemo:
    '''this class is developed by SHIVAM GUPTA for oop_in_python training tutorial'''    
    def __init__(self,name,id,age):    
        self.name = name;    
        self.id = id;    
        self.age = age    
    def display_details(self):    
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id,self.age))    
student_attr_demo = StudentBuiltinAttributesDemo("John",101,22)    
print(student_attr_demo.__doc__)    # It contains a string which has the class documentation
print(student_attr_demo.__dict__)   # It provides the dictionary containing the information about the class namespace.
print(student_attr_demo.__module__) # It is used to access the module in which, this class is defined.
print(student_attr_demo.__class__)  # It is used to access the class name.
###################################################################DESTRUCTOR IN PYTHON###########################################################################################################################################################################
#Example7.0: Here is the simple example of destructor. By using del keyword we deleted the all references of object ‘obj’, therefore destructor invoked explicitely.
class EmployeeDestructorDemo:
	# Initializing
	def __init__(self):
		print('Employee created.')
	# Deleting (Calling destructor)
	def __del__(self):
		print('Destructor called, Employee deleted.')
employee_destructor_demo = EmployeeDestructorDemo()
del employee_destructor_demo


#Example7.1:This example gives the explanation of above mentioned note. Here, notice that the destructor is called after the ‘Program End…/oop_in_python’ printed/automatically
class Employee_1:
	# Initializing
	def __init__(self):
		print('Employee created')
	# Calling destructor
	def __del__(self):
		print("Destructor called") #this will be printed at the last execution of file 'oops_in_python' when all statement gets executed
def Create_del_obj():
	print('Making Object...')
	obj_1 = Employee_1()
	print('function end...')
	return obj_1
print('Calling Create_del_obj() function...')
object_1= Create_del_obj()
print('Program End...')


#Example7.2:Python program to illustrate destructor In this example when the function fun() is called, it creates an instance of class B which passes itself to class A, which then sets a reference to class B and resulting in a circular reference.
'''class A:
  def __init__(self, bb):
    self.b2 = bb
  def m1(self):
    print("b2:",self.b2)
class B:
  def __init__(self):
    self.a = A("k")
  def m2():
      print("a:")       
  def __del__(self):
    print("die")
def fun():
	b1 = B()
fun()'''


############################################################################DYNAMIC ATTRIBUTE IN PYTHON####################################################################################################################################################################################
#Example8.0:The class “GFG” and all other objects or instances of this class do not know the attribute “name”. It is only defined for the instance “e2”.
class DynamicAttributeDemo:
	employee = True
 
# Driver Code
e1 = DynamicAttributeDemo()
e2 = DynamicAttributeDemo()
e1.employee = False
#e2.name = "Nikhil"#dynamically created attribue(name)/instance variable only for e2
print(e1.employee)
print(e2.employee)
#print(e2.name)
# this will raise an error as name is a dynamic attribute created only for the e2 object
#print(e1.name)

####################################################PYTHON MAGIC FUNCTIONS#############################################################################################################################################################################################################
#9.1:__init__ Method:After we have constructed an instance of the class, but before that instance is returned to the caller of the class, the _init_ method is executed. When we create an instance of the class, it is called automatically, just like constructors in various programming languages like the popular ones C++, Java, C#, PHP, etc. These methods are invoked after _new_ and therefore are referred to as initialising. We should define the instance parameters here.
class MagicInitDemo():  
  def __init__(self, *args):  
    print ("Now called __init__ magic method, after the initialised parameters")  
    self.name = args[0]  
    self.std = args[1]  
    self.marks = args[2]  
magic_init_student = MagicInitDemo("Itika", 11, 98)  
print(magic_init_student)  
print(type(magic_init_student))  
print(f"Name, standard, and marks of the student is: \n", magic_init_student.name, "\n", magic_init_student.std, "\n", magic_init_student.marks)  






#9.2:__new__() Method:The magic method __new__() is called implicitly by the __init__() method. The new instance returned by the __new__() method is initialised. To modify the creation of objects in a user-defined class, we must supply a modified implementation of the __new__() magic method.We need to provide the first argument as the reference to the class whose object is to be created for this static function.
class NewMethodDemo(object):
    def __new__(cls):
        print("Creating an instance by __new__ method")
        return super(NewMethodDemo, cls).__new__(cls)
    # Calling the init method
    def __init__(self):
        print("Init method is called here")
NewMethodDemo()







#9.3:__add__ Method:We use the magic method __add__to add the class instance's attributes. Consider the scenario where object1 belongs to class Method and object2 belongs to class Method_2, both of which have the same attribute called "attribute" that stores any value passed to the class while creating the instance. If specified to add the attributes, the __add__ function implicitly adds the instances' same attributes, such as object1.attribute + object2.attribute, when the action object1 + object2 is completed.Below is the code to show how we add two attributes of two instances of different classes without using the __add__ magic method.
# Python program to show how to add two attributes 

#without ___add___ method 
# Creating a class
class AddDemoNoMagicLeft:  
  def __init__(self, argument):  
   self.attribute = argument  
# Creating a second class  
class AddDemoNoMagicRight:  
  def __init__(self, argument):  
   self.attribute = argument  
# creating the instances  
no_magic_left_instance = AddDemoNoMagicLeft(" Attribute")  
print(no_magic_left_instance.attribute)  
no_magic_right_instance = AddDemoNoMagicRight(" 27")  
print(no_magic_right_instance.attribute)  
# Adding two attributes of the instances  
print(no_magic_left_instance.attribute + no_magic_right_instance.attribute)

#with ___add___ method
# Creating a class  
class AddDemoWithMagicLeft:  
   def __init__(self, argument):  
    self.attribute = argument  
   def __add__(self, object1):  
    return self.attribute + object1.attribute  
# Creating a second class  
class AddDemoWithMagicRight:  
   def __init__(self, argument):  
    self.attribute = argument  
   def __add__(self, object1):  
    return self.attribute + object1.attribute  
magic_left_instance = AddDemoWithMagicLeft(" Attribute")  
print(magic_left_instance)  
magic_right_instance = AddDemoWithMagicRight(" 27")  
print(magic_right_instance)  
print(magic_left_instance+ magic_right_instance) 








#9.4:__repr__ Method:The class instance is represented as a string using the magic method __repr__. The __repr__ method, which produces a string in the output, is automatically called whenever we attempt to print an object of that class.
# Python program to show how __repr__ magic method works  
# Creating a class  
class ReprDemo:  
# Calling __init__ method and initializing the attributes of the class  
  def __init__(self, x, y, z):  
   self.x = x  
   self.y = y  
   self.z = z  
# Calling the __repr__ method and providing the string to be printed each time instance is print  
  def __repr__(self): 
   return f"Following are the values of the attributes of the class ReprDemo:\nx = {self.x}\ny = {self.y}\nz = {self.z}"  
repr_instance = ReprDemo(4, 6, 2)  
print(repr_instance)







#9.5:__contains__ Method:The 'in' membership operator of Python implicitly calls the __contains__ method. We can use the __contains__ method to determine if an element is contained in an object's attributes. We can use this method for attributes that are containers ( such as lists, tuples, etc.).
# Python code to show how the __contains__ magic method works  
# Creating a class  
class ContainsDemo:  
# Calling the __init__ method and initializing the attributes  
  def __init__(self, attribute):  
    self.attribute = attribute  
    print("attribute is:",self.attribute)
# Calling the __contains__ method  
  def __contains__(self, attribute):  
    return attribute in self.attribute  
# Creating an instance of the class  
contains_instance = ContainsDemo([4, 6, 8, 9, 1, 6])   
# Checking if a value is present in the container attribute  
print("4 is contained in ""attribute"": ", 4 in contains_instance)  
print("5 is contained in ""attribute"": ", 5 in contains_instance)  
 
 






#9.6:__call__ Method:When a class instance is called, the Python interpreter calls the magic method __call__. We can utilise the __call__ method to explicitly call an operation using the instance name rather than creating an additional method to carry out specific activities.
# Python program to show how the __call__ magic method works  
# Creating a class  
class CallDemo:  
# Calling the __init__ method and initializing the attributes  
  def __init__(self, a): 
    self.a = a  
# Calling the __call__ method to multiply a number to the attribute value  
  def __call__(self, number):  
    return self.a * number  
# Creating an instance and proving the value to the attribute a  
callable_instance = CallDemo(7)  
print(callable_instance.a) # Printing the value of the attribute a  
# Calling the instance while passing a value which will call the __call__ method  
print(callable_instance(5))  







#9.7:__iter__ Method:For the given instance, a generator object is supplied using the __iter__ method. To benefit from the __iter__ method, we can leverage the iter() and next() methods.
# Python program to show how the __iter__ method works  
# Creating a class  
class IterDemo:  
   def __init__(self, start_value, stop_value):  
     self.start = start_value  
     self.stop = stop_value  
   def __iter__(self):  
     for num in range(self.start, self.stop + 1):  
        yield num ** 2  
# Creating an instance  
iter_instance = iter(IterDemo(3, 8))  
print( next(iter_instance) )  
print( next(iter_instance) )  
print( next(iter_instance) )  
print( next(iter_instance) )  
print( next(iter_instance) )  
print( next(iter_instance) )

######################################################OUTER_INNER CLASS IN PYTHON####################################################################################################################################################################################

#• without existing outer class object there is no scope of existing inner class object ,so we should declare the inner class inside the outer class(inner class is strongly associated with inner class )
#• we can define any number of inner classes inside the outer class
#• we can also define inner class inside the inner class(nested inner class) as:
#Example_10:
class Outer:
    def __init__(self):
          print("outer class object get created")
    def outer_method(self):
        pass
    class  Inner:
        def __init__(self):
            print("inner class object get created")
        def inner_method(self):
            print("inner class method get evoked")
_outer=Outer()         # OR                         i=Outer().Inner()       OR                    i=Outer().Inner().inner_method()
i=Outer.Inner()        #OR                          i.inner_method()        OR
i.inner_method()

######################################################DIFFERENCE BETWEEN 'HAS-A'& 'IS-A' RELATIONSHIP IN PYTHON#######################################################################################################################################################################
#1.The "has-a" relationship is a different type of relationship that is used to describe when one object contains another object. For example, a house has a door, so the House class would have a Door object as an attribute.(STRONGLY ASSOCIATED-COMPOSITION)
#Inheritance is an "is-a" relationship, which means that a child class inherits the properties and methods of its parent class. For example, a car is a type of vehicle, so the Car class inherits the properties and methods of the Vehicle class.
#Example_11:to demonstarte 'HAS-A' & 'IS-A' relationship in python oop
class PersonWithCar:# base class/container class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat_drink(self):
        print(self.name,"having age:",self.age,"is eating biryani and drinking beer at the restaurant")

class DriverWithCar(PersonWithCar):  # IS-A relationship[can extend to container class(Person) & can also use it)]/derived class(Driver)/contained class(driver 'IS-A' person) relationship exists](WEAK ASSOCIATION[]-AGGREGATION)
    def __init__(self,name,age,dno,dsal):
        super().__init__(name,age)
        self.dsal=dsal
        self.dno=dno
        self.car=DriverWithCar.Car("innova","2.5v","grey") # HAS-A relationship[having/containing object of class 'Car'& here(driver 'HAS-A' car) relationship exists]/WITHOUT EXISTING CONTAINER(DRIVER) CLASS THERE IS NO EXISTENCE OF CONTAINED CLASS(CAR)/ here driver class object contains car object directly
        #here d1=Driver("ravikant",34,1,25000)
        #here self.car is same as d1.Car("innova","2.5v","grey")
        #now can call car class object: self.car.getInfo()
        print("car object:",self.car)
    def driverInfo(self):
        print("driver sal",self.dsal)
        print("driver name",self.name)
        print("driver age",self.age)
        print("driver no",self.dno)
        print("driver car info") 
        self.car.getInfo()   # driver using car functionality
    class Car:
        def __init__(self,name,model,color):
            self.name=name
            self.model=model
            self.color=color  
        def getInfo(self):
            print('car name:{},model:{},color:{}'.format(self.name,self.model,self.color))
d1=DriverWithCar("ravikant",34,1,25000)
p1=PersonWithCar("SAMI",34) #optional since person is already instantaiated
d1.driverInfo() 
d1.eat_drink()
p1.eat_drink() 



#2.The "has-a" relationship is(WEAK ASSOCIATION-AGGREGATION) when without existing container class object(department) if there is existence of contained class object(professor).[department HAS-A professor(without existing department there is may be existence of professor)]   
class Professor:
    pass
class Department:
    def __init__(self,professor):
        self.professor=professor
        
prof1=Professor() #here 'prof_1' has independent existence/can exists independently
cs_dept=Department(prof1) #here 'cs_dept' contains reference(prof_1) of Proferrsor class
it_dept=Department(prof1) #note: if 'it_dept' is removed then there may be chance that 'prof_1' is working in 'cs_dept' or working independently(by using its own class)
         


#In 'Composition' container class objects holds directly contained class objects where as in 'Aggregation' container class objects holds reference of contained class objects

#########################################################INHERITENCE IN PYTHON###############################################################################################################################################################################################
#Example_12.0:simple Inheritence demonstration[Creating a Person class with Display methods.]
# A Python program to demonstrate inheritance
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


class PersonSimpleInheritance(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class EmployeeSimpleInheritance(PersonSimpleInheritance):

	# Here we return true
	def isEmployee(self): # pyright: ignore[reportIncompatibleMethodOverride]
		return True


# Driver code
per = PersonSimpleInheritance("Geek1") # An Object of Person
print(per.getName(), per.isEmployee())

emp = EmployeeSimpleInheritance("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())







#Example_12.1.1:Subclassing(calling constructor of Parent class)
# Python code to demonstrate how parent constructors are called.
# parent class
class PersonConstructorInheritance(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class
class EmployeeConstructorInheritance(PersonConstructorInheritance):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		PersonConstructorInheritance.__init__(self, name, idnumber) #  Super().__init__(self, name, idnumber) is also true


# creation of an object variable or an instance
a = EmployeeConstructorInheritance('Rahul', 'E886012', 200000, "Intern")

# calling a function of the class Person using its instance
a.display()




#Example_12.1.2:What iff we forget to do Subclassing(calling constructor of Parent class)?
#• If you forget to invoke the __init__() of the parent class then its instance variables would not be available to the child class. 
#• The following code produces an error for the same reason. 

'''
class A:
	def __init__(self, n='Rahul'):
		self.name = n


class B(A):
	def __init__(self, roll):            
		self.roll = roll


object = B(23)
print(object.name)

'''






#Example_12.2:Types of Inheritance in Python
#1.Single inheritance[Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code.]
# Base class
class ParentSingleInheritance:
	def func1(self):
		print("This function is in parent class.")

# Derived class
class ChildSingleInheritance(ParentSingleInheritance):
	def func2(self):
		print("This function is in child class.")


# Driver's code
child_single_object = ChildSingleInheritance()
child_single_object.func1()# child object can use base member
child_single_object.func2()




#2.Multiple inheritance[When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class. ]
#Base class1
class MotherMultipleInheritance:
	mothername = ""

	def mother(self):
		print(self.mothername)

# Base class2
class FatherMultipleInheritance:
	fathername = ""

	def father(self):
		print(self.fathername)

# Derived class
class SonMultipleInheritance(MotherMultipleInheritance, FatherMultipleInheritance):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)


# Driver's code
son_multiple = SonMultipleInheritance()
son_multiple.fathername = "RAM"  #accessing base class member(fathername)
son_multiple.mothername = "SITA" #accessing base class member(mothername)
son_multiple.parents()




#3.Multilevel inheritance[In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather. }
# Base class
class GrandfatherLineage:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername


# Intermediate class
class FatherLineage(GrandfatherLineage):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		GrandfatherLineage.__init__(self, grandfathername)


# Derived class
class SonLineage(FatherLineage):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		FatherLineage.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)


# Driver code
son_lineage = SonLineage('Prince', 'Rampal', 'Lal mani')
print(son_lineage.grandfathername)
son_lineage.print_name()





#4.Hierarchical inheritance[ When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child (derived) classes.]
# Base class
class ParentHierarchical:
	def func1(self):
		print("This function is in parent class.")

# Derived class1
class Child1Hierarchical(ParentHierarchical):
	def func2(self):
		print("This function is in child 1.")

# Derivied class2
class Child2Hierarchical(ParentHierarchical):
	def func3(self):
		print("This function is in child 2.")


# Driver's code
child1_object = Child1Hierarchical()
child2_object = Child2Hierarchical()
child1_object.func1()
child1_object.func2()
child2_object.func1()
child2_object.func3()




#5.Hybrid inheritance[Inheritance consisting of multiple types of inheritance is called hybrid inheritance.]
class School:
	def func1(self):
		print("This function is in school.")


class Student1(School):#single inheritence
	def func2(self):
		print("This function is in student 1. ")


class Student2(School):#hierarchical inheritence
	def func3(self):
		print("This function is in student 2.")


class child_Student1(Student1, School):#multiple inheritence
	def func4(self):
		print("This function is in student 3.")


# Driver's code
child_instance = child_Student1()
child_instance.func1()
child_instance.func2()


#########################################################ENCAPSULATION IN PYTHON###########################################################################################################################################################################
#Example_13: Python program to demonstrate encapsulation using private members 
# Creating a Base class
class Base:
    def __init__(self):
      self.a = "GeeksforGeeks"
      self.__c= "Geeky" #private member can't be accessed outside to this class & can be used by member functions only..
 
    def m1(self):
        print("private member of base is:",self.__c)

# Creating a derived class
class Derived(Base):
	def __init__(self):

		# Calling constructor of
		# Base class
		Base.__init__(self)
		print("Calling private member of base class: ")
		self.m1()


# Driver code
obj1 = Base()
print(obj1.a)
obj1.m1()

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
# is called inside derived class


#########################################################ABSTRACTION IN PYTHON##############################################################################################################################################################]
#Example_14.1: demo of abstration in python
import math
from abc import ABC, abstractmethod
class Shape(ABC): #here Shape is generalisation 
  """Abstract base class for all shapes."""

  @abstractmethod
  def area(self):
    """Abstract method to calculate the area of the shape."""

  @abstractmethod
  def perimeter(self):
    """Abstract method to calculate the perimeter of the shape."""

class RectangleDemo(Shape):
  """Concrete class for rectangles."""

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)

class CircleDemo(Shape):
  """Concrete class for circles."""

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * self.radius ** 2

  def perimeters(self):
    return 2 * math.pi * self.radius

# Create a rectangle object.
rectangle = RectangleDemo(5, 10)

# Calculate the area of the rectangle.
area_of_rectangle = rectangle.area()

# Print the area of the rectangle.
print(area_of_rectangle)


#Example_14.2: demo of abstration in python by importing user_defined Abstract Base Class
#implementaion class for Abstract Base Class 'Shape'
#note: we have to define abstract methods in subclasses otherwise it also becomes abstract class
import math
from Abstract2 import Shape as ImportedShape  # type: ignore
class RectangleImported(ImportedShape):
  """Concrete class for rectangles."""

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)

class CircleImported(ImportedShape):
  """Concrete class for circles."""

  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * self.radius ** 2

  def perimeters(self):
    return 2 * math.pi * self.radius


############################################################POLYMORPHISM IN PYTHON###############################################################################################################################
'''
#Example_15.0:no concept of 'method' overloading in python
def add(x, y,z):
    print("two arguments")
    return x + y+z


def add(x, y): #only this  function gets executed
    print("three arguments")
    return x + y

# Driver code
print(add(2,3))
print(add(2, 3, 4))
'''




#Example_15.1:Example of Polymorphism using in-built method
# Python program to demonstrate in-built poly-morphic functions
# len() being used for a string
print(len("geeks")) # here "geeks" takes string form but doing same work finding length

# len() being used for a list
print(len([10, 20, 30]))# here [10, 20, 30]  takes list form but doing same work finding length



#Example_15.2:Example of Polymorphism using class method
class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()


#Example_15.3:Example of Polymorphism using Inheritance
class Bird:
 def intro(self):
  print("There are many types of birds.")
	
 def flight(self):
  print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
 def flight(self):
  print("Sparrows can fly.")
	
class ostrich(Bird):
 def flight(self):
  print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()



#Example_15.4:Example of Polymorphism using function & objects
class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

# normal function
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

ferrari = Ferrari()
bmw = BMW()

car_details(ferrari)
car_details(bmw)



#Example_15.5.1:Example of Polymorphism using operator overloading
class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading + operator with magic method
    def __add__(self, other):
        return self.pages + other.pages  #b1.pages+b2.pages

b1 = Book(400)
b2 = Book(300)
print("Total number of pages: ", b1 + b2)

##Example_15.5.2:Example of Polymorphism using operator overloading(changing the behaviour of operator depending upon operands)
# add 2 numbers
print(100 + 200)

# concatenate two strings
print('Jess' + 'Roy')

# merger two list
print([10, 20, 30] + ['jessa', 'emma', 'kelly'])

#Example_15.6:Overrride Built-in Functions
class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):  # here 'len' is overriden
        print('Redefine length')
        count = len(self.basket)
        # count total items in a different way
        # pair of shoes and shir+pant
        return count * 2

shopping = Shopping(['Shoes', 'dress'], 'Jessa')
print(len(shopping))



##################################################################METACLASSES IN PYTHON##############################################################################################################################################














