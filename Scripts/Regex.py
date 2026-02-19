##################################################REGULAR EXPRESSION IN PYTHON######################################################################################################
'''

fullmatch()  : these are used when regex invoving total match of given string 
match()      : these are used when we have to read a string from user and check if the given string start with given string/regex or not

findall()
finditer()  : these are used when regex involving 'how many digits are available in the given strings'
search()

sub()       : these are used when regex involving 'replace the given string with regex &find the number of replacement'
subn()

split()     : these are used for replacement of given string with regex

'''

#Differencde between callabale iterator object and match/search(normal) object
#Example_0.1: Here is an example of how to use a normal object to search for a match in a string:
import re
string = "This is a test string."
pattern = re.compile(r"test")
match = pattern.search(string)
print(type(match))
print(match)
if match:
  #print(match)  not necessary!!!
  print(match.group())
  
 
  
#Example_0.2:Here is an example of how to use a caller object to search for a match in a string and to replace the match with a different string:
import re
string = "This is a test string."
pattern = re.compile(r"test")
match = pattern.finditer(string)
print(type(match))
print(match)
for match in match:
    print(match)
    print(match.group())
    
#Example_0.3:here is an example of 'list' object as re.findall()
import re
string = "This is a test string."
pattern = re.compile(r"test")
match = pattern.findall(string)
print(type(match))
print(match)
for match in match:
    print(match)
    #print(match.group()) wrong!!!



##############################################1.finditer()/compile()########################################################################################################################

#serching using the matcher object
#Example_1.1:
import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abaababa')  #matcher=re.finditer('ab','abaababa')
for match in matcher:
 count+=1
 print("start:{},end:{},group:{}".format(match.start(),match.end(),match.group()))
print("the number of occurence:",count)




#serching using the matcher object for string having metacharacter,special sequence & sets
#Example_1.2:
import re 
matcher=re.finditer('[^a-z]','a7b@k9z')
for match in matcher:
 print(match.start(),'....',match.group())


 
#Example_1.3:
import re 
matcher=re.finditer('a*','abaabaaab') #in string 'abaabaaab\n' here '\n' is also stored at 9th index
for m in matcher:
    print(m.start(),'..........',m.group())
 
 
    
#Example_1.4:
import re 
matcher=re.finditer('a{1,3}','abaabaaab') # minimum 1 a's & maximum 3 a's
for m in matcher:
    print(m.start(),'..........',m.group())
 
 
    
#Example_1.5:
import re 
matcher=re.finditer('^ab','abaabaaab') # check if 'abaabaaab' is starting with 'ab' or not
for m in matcher:
    print(m.start(),'..........',m.group())




#######################################################2.search()################################################################################################################



#Example_2.1: Searching a pattern in given string
import re
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)#match = re.search(pat, str), If the search is successful, search() returns a match object or None otherwise
if match:# If-statement after search() tests if it succeeded
  print('found  starting index:',match.start(),',found ending index:',match.end(),',founded string:', match.group()) # match.group() means'found word:cat'
else:
  print('did not find')
  


#Example_2.2:Search for pattern 'iii' in string 'piiig'.
##The search proceeds through the string from start to end, stopping at the first match found
## All of the pattern must match, but it may appear anywhere & also not all of the string
## On success, match.group() is matched text.
import re
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
match = re.search(r'igs', 'piiig') # not found, match == None
## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"
## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"



#Example_2.3:Group Extraction/matching
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str) #match = re.search(r'[\w.-]+@[\w.-]+', str)--## 'alice-b@google.com' (the whole match)
if match:
 print(match.group())   ## 'alice-b@google.com' (the whole match)
 print(match.group(1))  ## 'alice-b' (the username, group 1:left parenthesis match)
 print(match.group(2))  ## 'google.com' (the host, group 2:right parenthesis match)
 
 
 
 
#Example_2.4: Searching a pattern in given string
import re
str = 'an example word:CATat!!'
match = re.search(r'word:\w\w\w', str,re.IGNORECASE)
if match:# If-statement after search() tests if it succeeded
  print('found  starting index:',match.start(),',found ending index:',match.end(),',founded string:', match.group()) # match.group() means'found word:cat'
else:
  print('did not find')
  


 
  
###############################################3.match()###############################################################################################################

#Example_3.1:
import re
s=input("enter pattern to check:")
m=re.match(s,'abcdefgh')
if m!=None:
    print("match is available at the beginning of the string:{}".format(s))
    print('start_index:{} and end_index:{}'.format(m.start(),m.end()))
else:
    print("match is not available at the beginning of the string:")
 
 
    
##############################################4.fullmatch()################################################################################


#Example_4.1:
import re
s=input("enter pattern to check:")
m=re.fullmatch(s,'abcdefgh')
if m!=None:
    print("full string matched")
else:
    print("full string not matched:")
    
 
    
##############################################5.findall()########################################################################################

#Example_5.1:
import re 
matcher=re.findall('[0-9]','a7b9k6z') # create list of matched object
print("list is:",matcher)
for m in matcher:
    print("m:",m)
    

################################################6.sub()#########################################################################################
#Example_6.1:
import re
s=re.sub('\d','$','a7b9k5t9k') #sub(pattern,replacement,target) & returns the string after replacement 
print(s) 
 
###############################################7.subn()###################################################################################################################   
#Example_7.1: it returns the number of replacement in the string
import re
s=re.subn('\d','$','a7b9k5t9k') #t=sub(pattern,replacement,target) here it retuns object as 'tuple' having (resultstring,number of replacement) as an tuple value..
print(s)
print(type(s)) 
print("the result string:",s[0]) 
print("the number of replacement:",s[1]) 


###############################################8.split()#####################################################################################################################
#Example_8.1: it retuns object as list 
import re
l=re.split('\.','www.durgasoftvideos.com') #'[.]' is also same as '\.'  which means dot as a symbol only(anything inside a '[]'bracket is treated as symbol)
print(l)
for i in l:
    print(i)
  
  
  
  
    
###############################################Real-time application involving Regex###########################################################################################
#1.WAP to identify valid JAVA identifier
'''
RULES FOR VALID JAVA IDENTIFIER

i.the allowed character are:( -lowecase alphbets-digits-#)
ii.first character should be lowercase alphabet symbol from a to k
iii.the second character should be any digit divisible by 3
iv.the length of identifier should be atleast 2 

SOLUTION FOR VALID JAVA IDENTIFIER

ii.[a-k]
iii.[0369]
iv.[a-zA-Z0-9#]*
===>[a-k][0369][a-zA-Z0-9#]* is the required Regex
'''
import re
s=input("enter identifier to validate:")
m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
if m!= None:
    print(s,":is valid java identifier")
else:
    print(s,":is not valid java valid identifier")
    
 
 
 
    
    
#2.1:WAP to identify valid mobile number
'''
RULES FOR VALID MOBILE NUMBER

i. the mobile number should be of length 10
ii.should contain digits between 0-9
iii.first digit should be between(6,7,8,9)

SOLUTION FOR VALID MOBILE NUMBER

iii.[6789]
===>[6789][0-9]{9} or [6-9]\d{9} is the required regex
'''
import re
s=input("enter mobile number to validate:")
m=re.fullmatch('[6-9]\d{9}',s)
if m!= None:
    print(s,":is valid mobile number")
else:
    print(s,":is not valid mobile number")
    
 
 
 
 
 
 
    
#2.2:WAP to identify valid mobile number of 10, 11, 12 or 13 digit
'''
#RULES FOR VALID MOBILE NUMBER

i. if the length of mobile number is 10 then first digit should be between(6,7,8,9)
ii.if the length of mobile number is 11 then first digit should be 0 & rest digit should follow above rule i
iii.if the length of mobile number is 12 then first  two digit should be 91 & rest digit should follow above rule i
iv.if the length of mobile number is 13 then first three digit should be +91 & rest digit should follow above rule i


SOLUTION FOR VALID MOBILE NUMBER

i.[6-9]\d{9}
ii.0{1}[6-9]\d{9}
iii.91[6-9]\d{9}
iv.=91[6-9]\d{9}
'''
import re
s=input("enter mobile number to validate:")
if len(s)==10:
  m=re.fullmatch('[6-9]\d{9}',s)
  if m!= None:
      print(s,":is valid mobile number")
  else:
    print(s,":is not valid mobile number")
           
elif len(s)==11:
    m=re.fullmatch('0{1}[6-9]\d{9}',s)
    if m!= None:
        print(s,":is valid mobile number")
    else:
        print(s,":is not valid mobile number")
elif len(s)==12:
    m=re.fullmatch('91[6-9]\d{9}',s)
    if m!= None:
        print(s,":is valid mobile number")
    else:
        print(s,":is not valid mobile number")
elif len(s)==13:
    m=re.fullmatch('+91[6-9]\d{9}',s)
    if m!= None:
        print(s,":is valid mobile number")
    else:
        print(s,":is not valid mobile number")        
else:
    print("invalid mobile number")
    
    
    



   
#3:WAP to read 'input_file.txt' & write all the mobile number from it to 'output_file.txt'
import re
f1=open('input_file.txt','r')
f2=open('output_file.txt','w')
for line in f1:
    list=re.findall('[6-9]\d{9}',line)
    for number in list:
        f2.write(number+"\n")
print("extracted all mobile number from 'input_file.txt' & written into 'output_file.txt':")
f1.close()
f2.close()








#4:WAP to check valid email-id
import re
s-input("enter e-mail id:")
m=re.fullmatch('\w[a-zA-Z0-9_.]*@(gmail|rediffmail)[.][a-z]+',s) # first letter of local name should be either alphanumeric or underscore( so used here '\w')
if m!=None:
    print("valid e-mail id")
else:
    print("invalid e-mail id")









#5.1:web scrapping(collecting informationn from web pages) by regular expression
import re,urllib
import urllib.request
sites=['https://www.google.com/','https://www.rediff.com/','https://www.redbus.in/']
for site in sites:
    print("searching.....",site)
    u=urllib.request.urlopen(site)
    text=u.read()
    #print(text)
    #print(type(text))
    title = re.findall("<title>.*</title>", text.decode('utf-8'), re.IGNORECASE)
    print(title[0])
 




    

#5.2 WAP to read all mobile number from  redbus.in using web scrapping
import re,urllib
import urllib.request
u=urllib.request.urlopen('https://www.redbus.in/')
text=u.read()
numbers=re.findall('[0-9]{3,4}[-| ][0-9]{8}',text.decode('utf-8'),re.IGNORECASE)
for num in numbers:
    print(num)

