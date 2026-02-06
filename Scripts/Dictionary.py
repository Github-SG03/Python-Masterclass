##############################dictionary in python###############################################
#creating a simple dictionary
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)  

# Creating an empty Dictionary   
Dict = {}   
print("Empty Dictionary: ")   
print(Dict)    
# Creating a Dictionary  
# with dict() method   
Dict = dict({1: 'Java', 2: 'T', 3:'Point'})   
print("\nCreate Dictionary by using  dict(): ")   
print(Dict)  

# Creating a Dictionary   
# with each item as a Pair   
Dict = dict([(1, 'Devansh'), (2, 'Sharma')])   
print("\nDictionary with each item as a pair: ")   
print(Dict) 

#accessing the dictionary element
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))  
print("printing Employee data .... ")  
print("Name : %s" %Employee["Name"])  
print("Age : %d" %Employee["Age"])  
print("Salary : %d" %Employee["salary"])  
print("Company : %s" %Employee["Company"]) 



#modifing dictionary
# Creating an empty Dictionary   
Dict = {}   
print("Empty Dictionary: ")   
print(Dict)     
# Adding elements to dictionary one at a time   
Dict[0] = 'Peter'  
Dict[2] = 'Joseph'  
Dict[3] = 'Ricky'  
print("\nDictionary after adding 3 elements: ")   
print(Dict)      
# Adding set of values    # with a single Key   # The Emp_ages doesn't exist to dictionary  
Dict['Emp_ages'] = 20, 33, 24  #adding tuple as a value to key('Emp_ages') 
print("\nDictionary after adding 3 tuple elements: ")   
print(Dict)
Dict['Emp_Marks']={22,33,44} 
print("\nDictionary after adding 3 set elements: ")   
print(Dict)   
Dict['Emp_City']=['Pune','Varanasi','Delhi'] 
print("\nDictionary after adding 3 list elements: ")  
print(Dict)   
Dict['emp_mob']={1:"9140889870",2:"7559424177",3:"7081469030"}
print("\nDictionary after adding 3 dict elements: ")  
print(Dict) 
# Updating existing Key's Value   
Dict[3] = 'JavaTpoint'  
print("\nUpdated key value: ")   
print(Dict)   

#Another example for update
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)    
print("Enter the details of the new employee....");    
Employee["Name"] = input("Name: ");    
Employee["Age"] = int(input("Age: "));    
Employee["salary"] = int(input("Salary: "));    
Employee["Company"] = input("Company:");    
print("printing the new data");    
print(Employee)


#deleting the dictionary element
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
print(type(Employee))    
print("printing Employee data .... ")    
print(Employee)    
print("Deleting some of the employee data")     
del Employee["Name"]    
del Employee["Company"]    
print("printing the modified information ")    
print(Employee)    
print("Deleting the dictionary: Employee");    
del Employee  
print("Lets try to print it again ");    
#print(Employee) 


#Built-in Dictionary functions
empl1={"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
empl2={"Name": "Abraham", "Age": 47, "salary":55000,"Company":"MICROSOFT"}
#print(cmp(empl1,empl2))
print(len(empl1))
print(str(empl1))
print(type(empl1))

#Built-in Dictionary method
empl2={"Name": "Abraham", "Age": 47, "salary":55000,"Company":"MICROSOFT"}
print(empl2.items())#
print(empl2.values())#
print(empl2.keys())#
print(empl2.copy())#
print(empl1.clear())#
empl2.update({'max':50})#
print(empl2)
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq, 10)#
print("New Dictionary : %s" %str(dict))
dict = {'Name': 'Zabra', 'Age': 7}#
print("Value : %s" %  dict.get('Age'))
print("Value : %s" %  dict.get('Education', "Never"))
empl2.pop("Age")#
print(empl2)
#print(empl2.count(47))#
#print(empl2.index(47))#
#print(empl2.popitem(55000))#




#the key cannot be any mutable object
""""
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",[100,201,301]:"Department ID"}    
for x,y in Employee.items():    
    print(x,y)

"""

###example1 for dictionary iteration
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
for x in Employee:    
    print(Employee[x]) 
    
    
####example2  for dictionary iteration
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}    
for x in Employee.values():    
    print(x)  
    
    
#1.Nested Dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child1"]['name'])
#2.Nested Dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child1"]['name'])
##Accesing Dictionary Element
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, y in myfamily.items():
    print(x,y)
    
   
    
















     


     