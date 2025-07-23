############################List in python#########################################################
#simple list snippet
l1 = ["John", 102, "USA"]    
print(l1) 
print(type(l1))

#compare two lists
a = [1,2,"Peter",4.50,"Ricky",5,6]  
b = [1,2,5,"Peter",4.50,"Ricky",6]  
print(a ==b) # both are not same as they are unorderd although having same element
 
#Let's have a look at the list example in detail.
emp = ["John", 102, "USA"]     
Dep1 = ["CS",10]  
Dep2 = ["IT",11]    
HOD_CS = [10,"Mr. Holding"]    
HOD_IT = [11, "Mr. Bewon"]    
print("printing employee data...")    
print("Name : %s, ID: %d, Country: %s"%(emp[0],emp[1],emp[2]))    
print("printing departments...")   
print("Department 1:\nName: %s, ID: %d\nDepartment 2:\nName: %s, ID: %s"%(Dep1[0],Dep2[1],Dep2[0],Dep2[1]))    
print("HOD Details ....")    
print("CS HOD Name: %s, Id: %d"%(HOD_CS[1],HOD_CS[0])) #print("CS HOD Name:{}, Id: {}".format(HOD_CS[1],HOD_CS[0]))   
print("IT HOD Name: %s, Id: %d"%(HOD_IT[1],HOD_IT[0]))    
print(type(emp),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_IT))  

#list slicing example
list = [1,2,3,4,5,6,7]  
print(list[0])  
print(list[1])  
print(list[2])  
print(list[3])  
print(list[0:6])# Slicing the elements    
print(list[:]) # By default the index value is 0 so its starts from the 0th element and go for index -1.   
print(list[2:5])  
print(list[1:6:2]) 
mystr = "Hello"
print(mystr[:-3])#He
print(mystr[-4:-3])#e 
print(mystr[-4:-2:1])# el #same as mystr[-4:-2]
print(mystr[::-1])#olleH
print(mystr[::-2])#olH
print(mystr[-4::-2])#e
print(mystr[-4::-1])#eH
print(mystr[-4:-3:-1])#


#updating list values
list = [1, 2, 3, 4, 5, 6]     
print(list)     
# It will assign value to the value to the second index   
list[2] = 10   
print(list)    
#Adding multiple-element   
list[1:3] = [89, 78] #list[1:3] = 89,78 (also true)  
print(list)   
# It will add value at the end of the list  
list[-1] = 25  
print(list)  

#del list element or entire list
del list[-1]
print(list)
lists=['1','3','9']
del lists
#print(lists)

#python list operation
l1=[1,2,3,4]#list of natural number upto 5
l2=[2,4,8,10]# list of even number upto 10
print(l1+l2)
print(l1*2)
print(len(l1))
print(10 in l2)
print(l1==l2)
for i in l1:
    print(i)
    
##adding the element at the end of empty list    
#Declaring the empty list  
l =[]  
#Number of elements will be entered by the user    
n = int(input("Enter the number of elements in the list:"))  
# for loop to take the input  
for i in range(0,n):     
    # The input is taken from the user and added to the list as the item  
    l.append(input("Enter the item:"))     
print("printing the list items..")   
# traversal loop to print the list items    
for i in l:   
    print(i, end = "  ") 
    
    
#removing the element from the listr'
l = [56,66,77,88]     
print("\nprinting original list: ");    
for i in l:    
    print(i,end=" ")    
l.remove(66)    
print("\nprinting the list after the removal of first element...")    
for i in l:    
    print(i,end=" ") 
    

#python program to show built in function & method(here we are using separate 'print' bcoz 'list' is mutable & 'string' is not)
#bulit in function
list1, list2 = [123, 'xyz'], [456, 'abc']
list3, list4 = [123, 456], [456, 678]
t1=(5,6,8)  
#print(cmp(l1=l2))
#print(seq(t1))
print(len(list1))
print(min(list3))
print(max(list4))
print(type(list1))

#built in method
list1, list2 = [123, 'xyz'], [456, ]
tuples1=(5,6,8)
list1.append(2)
print(list1)
list1.remove(2)
print(list1)
list1.insert(2,"banana")
print(list1)
list1.extend([1,2])
print(list1)
list1.pop(1)
print(list1)
print(list1.count('xyx'))
list1.reverse()
print(list1)
print(list2.copy())
print(list2.index(456))
list2.sort()
print(list2)
list1.clear()
print(list1)

#python program to print list having unique element from the given list
list1 = [1,2,2,3,55,98,65,65,13,29]  
# Declare an empty list that will store unique values  
list2 = []  
for i in list1:  
   if i not in list2:  
    list2.append(i)  
print(list2)  


#Write the program to find the lists consist of at least one common element.
list1 = [1,2,3,4,5,6]  
list2 = [7,8,1,9,2,10]  
for i in list1:  
 for j in list2:  
  if i == j:  
    print("The common element is:",i) 


#list comprehension
fruits=['banana','apple','guava','pomegranates']
newlist = [x for x in fruits if x != "apple"]  
print(newlist)                                                  
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
#The condition is optional and can be omitted:











