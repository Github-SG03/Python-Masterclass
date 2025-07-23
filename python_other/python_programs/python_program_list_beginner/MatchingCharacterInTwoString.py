# First, we will define the count function  
def count_1(string_1, string_2):   
    count, find_1 = 0, 0  
        
# The loop will execute till the length of string_1 and it will   
# Stores the value of string_1 character by character and stores in "store_1" at every iteration.  
    for store_1 in string_1:      
            
        # This will check if the extracted from of the characters of string_1   
        # is present in string_2 or not.  
        if string_2.find(store_1) >= 0 and find_1 == string_1.find(store_1):   
            count += 1  
        find_1 += 1  
    print ('The no. matching characters in the pairs of strings: ', count)  
    
# Main function  
def main():   
    string_1 = str(input ("Please enter the characters for String 1: "))  
    string_2 = str(input ("Please enter the characters for String 2: "))  
    count_1(string_1, string_2) # At last, calling the count function  
  
    
# Driver Code  
if __name__ == "__main__":  
    main()  