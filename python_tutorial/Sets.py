######################sets in Python#######################################################
sets= set() #creating an empty set
print(type(sets)) 

Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
print(Days)  #data items are unique & unordered(Days = {"Sonday", "Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday"}    ) 
print(type(Days))    
print("looping through the set elements ... ") #we cannot access the particular element in sets(as there is no indexing in sets) but can access the entire sets    
for i in Days:    
    print(i)
 
 
    
#creating sets of immutable type as it contain immutable objects not mutable like(list,dictionary)
#Creating a set which have immutable elements  
set1 = {1,2,3, "JavaTpoint", 20.5, 14}  
print(type(set1))  
#Creating a set which have mutable element  
#set2 = {1,2,3,["Javatpoint",4]}  
#print(type(set2)) 

##Python Set Operations 
#union
Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
Days2 = {"Friday","Saturday","Sunday"}    
print(Days1|Days2) #printing the union of the sets using |     	
Days1={"Monday","Tuesday","Wednesday","Thursday"}    
Days2 = {"Friday","Saturday","Sunday"}
print(Days1.union(Days2)) #printing the union of the sets using union() 

#intersection
Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
print(Days1&Days2) #prints the intersection of the two sets using &
set1 = {"Devansh","John", "David", "Martin"}    
set2 = {"Steve", "Milan", "David", "Martin"}    
print(set1.intersection(set2)) #prints the intersection of the two sets using intersection()           
#intersection_update(reslts new set)
a = {"Devansh", "bob", "castle"} # "Devansh", "bob", "castle" should be in b&c  
b = {"castle", "dude", "emyway"}    
c = {"fuson", "gaurav", "castle"}        
print(a.intersection_update(b, c)) 

#difference 
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1-Days2) #{"Wednesday", "Thursday" will be printed} using '-'
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday", "Sunday"}    
print(Days1.difference(Days2)) # prints the difference of the two sets Days1 and Days2 using difference()


#symmetric difference
a = {1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a^b  
print(c)  
a={1,2,3,4,5,6}  
b = {1,2,9,8,10}  
c = a.symmetric_difference(b)
print(c)


#set comparison
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
Days2 = {"Monday", "Tuesday"}    
Days3 = {"Monday", "Tuesday", "Friday"}         
#Days1 is the superset of Days2 hence it will print true.     
print (Days1>Days2)       
#prints false since Days1 is not the subset of Days2     
print (Days1<Days2)    
#prints false since Days2 and Days3 are not equivalent     
print (Days2 == Days3)  


#Frozenset(mutable set)
Frozenset = frozenset([1,2,3,4,5])     
print(type(Frozenset))    


#set built-in method
a = {1,2,3,4,5,6}  
a.add(7)#It adds an item to the set. It has no effect if the item is already present in the set.
print(a)
print(a.copy())#It returns a shallow copy of the set.
a.discard(1)#It removes the specified item from the set.
print(a)
a.pop()#Remove and return an arbitrary set element that is the last element of the set. Raises KeyError if the set is empty.
print(a)
a.remove(3)#Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.
print(a)
a.update((8,9,10))#accepts any iterable as an argument
print(a)








 
           

        