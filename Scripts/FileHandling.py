#################################################FILE HANDLING IN PYTHON######################################################
##################################################################################################################################################################################################################################################################################
#Example_1.1:opening the file & check if its is open successfully or not (if it is available in directory)
#opens the file file.txt in read mode    
fileptr = open("file_1.txt","r")    
if fileptr:   
 print("file is opened successfully so as name & fileno of the file is:",fileptr.name,fileptr.fileno)  
 
 
#Example_1.2:opening the file & check if its is open successfully or not (if it is available in directory then throw boolean 'True' value otherwise 'False' to fileobject) & close it if it open successfully
# opens the file file.txt in read mode    
fileptr = open("file_1.txt","r")    
if fileptr:    
 print("file is opened successfully")    
#closes the opened file    
fileptr.close()  
 
 
#Example_1.3:opening the file & check if its is open successfully or not (if it is available in directory then throw boolean 'True' value otherwise 'False' to fileobject) & do not need to close it if it open successfully as automatically close the file
#opens the file file.txt in read mode(always open the file using 'with' as it provides the guarantee to close the file regardless of how the nested block exits.)
with open("file_1.txt",'r') as f:    
    content = f.read();    
print(content) 





'''
#Example_1.4
#return the next line from the file using 'next()'
fileptr = open("file_1.txt","r")   
content=fileptr.readline()
#prints the first line of the file 
print(content)
#stores next line from begining of the file into the variable content  
content = fileptr.next()      
#prints the next line after the first line of the file    
print(content)       
#closes the opened file    
fileptr.close() 
''' 

 


#Example_1.5
#open the file_2.txt in read mode. causes error if no such file exists.    
fileptr = open("file_2.txt","r")  
#stores all the data upto 10 characters from begining of the file into the variable content    
content = fileptr.read(10)   
#prints the type of the data stored in the file    
print(type(content))      
#prints the content of the file    
print(content)       
#closes the opened file    
fileptr.close()  


#Example_1.6
#We can read the file using for loop. Consider the following example.
#open the file.txt in read mode. causes an error if no such file exists.    
fileptr = open("file_1.txt","r");     
#running a for loop     
for i in fileptr:    
 print(i) # i contains each line of the file 
 
 
#Example_1.7
#open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file_4.txt","w+");     
#stores  the first & second line of the file into the variable content & content_1 respectively    
content = fileptr.readline()     
content1 = fileptr.readline()  
#prints the content(first & second line) of the file    
print(content)     
print(content1)  
#closes the opened file    
fileptr.close() 



#Exaple_1.8
#open the file.txt in read mode. causes error if no such file exists.    
fileptr = open("file_3.txt","r");         
#stores all the data of the file into the variable content    
content = fileptr.readlines()       
#prints the content of the file    
print(content)     
#closes the opened file    
fileptr.close() 



#Example_1.9
#truncate()-It truncates the file to the optional specified size.
f = open("demofile2.txt", "r+")
f.truncate(2)
#open and read the file after the truncate:
f = open("demofile2.txt", "r")
print(f.read())
f.close()


         

##########################################################################################################################################################################################################################################################################################
#Example_2.1.1:open the file.txt in 'write' mode. Create a new file if no such file exists.(using 'write()', we can write single line on file)  
fileptr = open("file_7.txt", "w")   
# appending the content to the file  
fileptr.write('''Python is the modern day language. It makes things so simple. 
It is the fastest-growing programing language\n''')   
#closing the opened the file  
fileptr.close() 


#Example_2.1.2:open the file.txt in 'write' mode. Create a new file if no such file exists.(using 'write()', we can write single line on file)  
fileptr = open("file_6.txt", "w")   
# appending the content to the file 
for i in range(11): 
   fileptr.write('''Python is the modern day language. It makes things so simple. It is the fastest-growing programing language\n''')  #using the 'for' loop to write multiple line on the file
#closing the opened the file  
fileptr.close() 



#Example_2.2:open the file.txt in 'write' mode. Create a new file if no such file exists.(using 'writelines()', we can write multiple line on file)    
fileptr = open("file_5.txt", "w")   
# appending the content to the file  
fileptr.writelines(""" cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
cpytho is the modern day language. It makes things so simple. It is the fastest-growing programing language
""")   
#closing the opened the file  
fileptr.close() 





#################################################################################################################################################################################################################################################################################################
#Example_3.1
#File Pointer positions using tell()
#open the file file2.txt in read mode    
fileptr = open("file_3.txt","r")    
#initially the filepointer is at 0     
print("The filepointer is at byte :",fileptr.tell())    
#reading the content of the file    
content = fileptr.read();    
#after the read operation file pointer modifies. tell() returns the location of the fileptr.          
print("After reading, the filepointer is at:",fileptr.tell())    


#Example_3.2
#Modifying file pointer position using seek()
#open the file file_2.txt in read mode    
fileptr = open("file_2.txt","r")    
#initially the filepointer is at 0     
print("The filepointer is at byte :",fileptr.tell())    
#changing the file pointer location to 10.    
fileptr.seek(10);    
#tell() returns the location of the fileptr.     
print("After reading, the filepointer is at:",fileptr.tell())  

################################################################################################################################################################################################################################################
'''
#Example_4.1: Python OS Module
#renaming the file
import os       
#rename file_4.txt to file_II.txt    
os.rename("file_4.txt","file_IV.txt") 
'''



'''
#Example_4.2: Python OS Module
#Removing the file
import os;    
#deleting the file named file3.txt     
os.remove("file3.txt") 
'''



'''
#Example_4.3: Python OS Module
#creating a new directory
import os      
#creating a new directory with the name 'new' in current directory    
os.mkdir("new") 
'''



'''
#Example_4.4: Python OS Module
#return the current working directory
import os  
os.getcwd() 
'''




'''
#Example_4.5: Python OS Module
#Changing the current working directory to a specific directory
import os   
# Changing current directory with the new directiory  
os.chdir("C:\\Users\\DEVANSH SHARMA\\Documents")  
'''


'''
#Example_4.6: Python OS Module
#deleting a directory
import os  
#removing the new directory     
os.rmdir("directory_name")   
'''

##########################################################################################################################################################################################################################################

#Writing Python script output to the files
#The check_call() method of module subprocess is used to execute a Python script and write the output of that script to a file.
import subprocess     
with open("output.txt", "wb") as f:    
    subprocess.check_call(["python", "output_pythonscript.py"], stdout=f)# here output of  'output_pythonscript' is stored in 'output.txt' when we run this file(file_Handlin.py)
 

#####################################################################################################################################################################################################################################################
#The file related methods
#The file object provides the following methods to manipulate the files on various operating systems.

'''
#SN	Method	Description
1	file.close()	It closes the opened file. The file once closed, it can't be read or write anymore.
2	File.fush()	It flushes the internal buffer.
3	File.fileno()	It returns the file descriptor used by the underlying implementation to request I/O from the OS.
4	File.isatty()	It returns true if the file is connected to a TTY device, otherwise returns false.
5	File.next()	It returns the next line from the file.
6	File.read([size])	It reads the file for the specified size.
7	File.readline([size])	It reads one line from the file and places the file pointer to the beginning of the new line.
8	File.readlines([sizehint])	It returns a list containing all the lines of the file. It reads the file until the EOF occurs using readline() function.
9	File.seek(offset[,from)	It modifies the position of the file pointer to a specified offset with the specified reference.
10	File.tell()	It returns the current position of the file pointer within the file.
11	File.truncate([size])	It truncates the file to the optional specified size.
12	File.write(str)	It writes the specified string to a file
13	File.writelines(seq)	It writes a sequence of the strings to a file.
'''

############################################################################################################################################################################################################################################################################################################
#################################################operation on CSV FILE################################################
#CSV FILE(A csv stands for "comma separated values", which is defined as a simple file format that uses specific structuring to arrange tabular data. It stores tabular data such as spreadsheet or database in plain text and has a common format for data interchange. A csv file opens into the excel sheet,  the rows and columns data define the standard format.)
#Python CSV Module Functions
'''
• The CSV module work is used to handle the CSV files to read/write and get data from specified columns. There are different types of CSV functions, which are as follows:
	* csv.field_size_limit - It returns the current maximum field size allowed by the parser.
	* csv.get_dialect - It returns the dialect associated with a name.
	* csv.list_dialects - It returns the names of all registered dialects.
	* csv.reader - It read the data from a csv file
	* csv.register_dialect - It associates dialect with a name. The name must be a string or a Unicode object.
	* csv.writer - It writes the data to a csv file
	* o csv.unregister_dialect - It deletes the dialect which is associated with the name from the dialect registry. If a name is not a registered dialect name, then an error is being raised.
	* csv.QUOTE_ALL - It instructs the writer objects to quote all fields. csv.QUOTE_MINIMAL - It instructs the writer objects to quote only those fields which contain special characters such as quotechar, delimiter, etc.
	* csv.QUOTE_NONNUMERIC - It instructs the writer objects to quote all the non-numeric fields.
    * csv.QUOTE_NONE - It instructs the writer object never to quote the fields.
'''

#Reading CSV files 
# 'csv.reader()'-In Python, the csv.reader() module is used to read the csv file. It takes each row of the  csv file and makes a list of all the columns.
#We have taken a txt file named as python.txt that have default delimiter comma(,) with the following data:
'''
name,department,birthday month    
Parker,Accounting,03-03-1999,November    
Smith,IT,01-04-2000,October  

'''
import csv    
with open('Python_FileHandling_Read.csv','r') as csv_file:    
 csv_reader = csv.reader(csv_file, delimiter=',')    #returns value as [' ',' ',' ',' '] to 'csv_reader' variable
 row_count = 0    
 for row in csv_reader:
  #print(row)    
  if row_count == 0:    
   print(f'Column names are {", ".join(row)}')    
   row_count += 1
  else:
   print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}')             
   row_count += 1    
 print(f'Processed {row_count} lines.')
 
#Writing CSV Files
#Let's write the following data to a CSV File.
'''
data = [{'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'},     
        {'Rank': 'A', 'first_name': 'Smith', 'last_name': 'Rodriguez'},    
        {'Rank': 'C', 'first_name': 'Tom', 'last_name': 'smith'},    
        {'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},     
        {'Rank': 'A', 'first_name': 'Alex', 'last_name': 'Tim'}]  
'''  
#It presents two functions, i.e., writerow() and writerows(). The writerow() function only write one row, and the writerows() function write more than one row.
import csv          
with open('Python.csv', 'w') as csv_file: 
 field_name = ['Rank','first_name', 'last_name']   
 csv_writer = csv.DictWriter(csv_file,field_name,delimiter = ',')    
 csv_writer.writeheader()    
 csv_writer.writerow({'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'})    
 csv_writer.writerow({'Rank': 'A', 'first_name': 'Smith','last_name': 'Rodriguez'}) 
 csv_writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})    
 csv_writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
print("Writing complete")          
 
 
 
 

    










 




   

  
 









 
 
 