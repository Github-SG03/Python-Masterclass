class Car:    # here, we are declaring a class named car  
    def __init__(self, make, model, year):    
        self.make = make        
# Here, we are using the self to declare the make variables locally  
        self.model = model    
# Here, we are using the self to declare the model variables locally  
        self.year = year      
# Here, we are using the self to declare the year variables locally  
    def __str__(self):    
        return str.format("Make: {}, Model: {}, Year: {}", self.make, self.model, self.year)    
   # Here, we are returning the format of the strings given  
def merge(list1, l, r, m, comp_fun):    
# Here, we are defining a function for merge the list using the compound function   
    left_copy = list1[l:m + 1]      # here, we are coping the left part of the list  
    r_sublist = list1[m+1:r+1]   # here, we are coping the right part of the list  
    left_copy_index = 0     # here, we are coping the left part indexes of the list  
    r_sublist_index = 0     # here, we are coping the right part indexes of the list  
    sorted_index = l    
    while left_copy_index < len(left_copy) and r_sublist_index < len(r_sublist):    
# Here, we are declaring a while loop  
        # Here, we are using the comp_fun instead of a simple comparison operator    
        if comp_fun(left_copy[left_copy_index], r_sublist[r_sublist_index]):    
# Here, we are checking the if condition, if it is true then we will enter the block  
            list1[sorted_index] = left_copy[left_copy_index]    
            left_copy_index = left_copy_index + 1    
        else:    # if the condition is false then we will enter the else block  
            list1[sorted_index] = r_sublist[r_sublist_index]    
            r_sublist_index = r_sublist_index + 1    
        sorted_index = sorted_index + 1    
    while left_copy_index < len(left_copy):     # Here, we are declaring a while loop  
        list1[sorted_index] = left_copy[left_copy_index]    
        left_copy_index = left_copy_index + 1    
        sorted_index = sorted_index + 1   
    while r_sublist_index < len(r_sublist):      # Here, we are declaring a while loop  
        list1[sorted_index] = r_sublist[r_sublist_index]    
        r_sublist_index = r_sublist_index + 1    
        sorted_index = sorted_index + 1    
def merge_sort(list1, l, r, comp_fun):    
# Here, we are declaring the merge sort function to sort the given list  
    if l >= r:   
# Here, we are checking the if condition, if it is true then we will enter the block  
        return    
    m = (l + r)//2     # here, we are finding the middle element of the list  
    merge_sort(list1, l, m, comp_fun)     
# Here, we are calling the merge sort function till the middle number we got     
    merge_sort(list1, m + 1, r, comp_fun)    
# Here, we are calling the merge sort function from the middle number we got  
    merge(list1, l, r, m, comp_fun)    
# Here, we are calling the merge function to merge the divided list using the merge   # sort function above  
car1 = Car("Renault", "33 Duster", 2001)    
car2 = Car("Maruti", "Maruti Suzuki Dzire", 2015)    
car3 = Car("Tata motor", "Jaguar", 2004)    
car4 = Car("Cadillac", "Seville Sedan", 1995)    
list1 = [car1, car2, car3, car4]    
merge_sort(list1, 0, len(list1) -1, lambda carA, carB: carA.year < carB.year)    
print("Cars sorted by year:")    
for car in list1:     # here, we are declaring the for loop to iterate through list1  
    print(car)     # here, we are printing all the data of the car and the list  
print()    
merge_sort(list1, 0, len(list1) -1, lambda carA, carB: carA.make < carB.make)    
print("Cars sorted by make:")    
for car in list1:  # here, we are declaring the for loop to iterate through list1  
    print(car)     # here, we are printing all the data of the car and the list    