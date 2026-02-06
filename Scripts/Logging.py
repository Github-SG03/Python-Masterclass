#############################LOGGING IN PYTHON###################################################

#Example_0:
#Logging: Variable data
import logging
name = 'John'
logging.error('%s raised an error', name)



'''#Example_1: without any formating
# WAP to create a log file and write 'warning' & higher logging level messages

# importing module
import logging
 
# Create and configure logging file
logging.basicConfig() #we can use 30 instead of logging.WARNING & default logging filemode is 'a' & when we use only 'logging.basicConfig()' then it will print all the logging level msg on console

# simple Test messages
print("logging in python demo_1") 
           
# log messages
logging.debug("Harmless debug Message")        # it is not going to be printed as logging level set as 'logging.WARNING'
logging.info("Just an information")            # it is not going to be printed as logging level set as 'logging.WARNING'
logging.warning("Its a Warning")
logging.error("Did you try to divide by zero")
logging.critical("Internet is down")
'''




'''
#Example_2:  formating with for default logging message & with  explicite filemode
#This code demonstrates all the levels of logging.

# importing module
import logging
 
# Create and configure logging file
logging.basicConfig(filename="newfile_1.log", level=logging.WARNING,filemode='w') #we can use 30 instead of logging.WARNING

# simple Test messages
print("logging in python demo_2") 
           
# log messages
logging.debug("Harmless debug Message")       
logging.info("Just an information")            
logging.warning("Its a Warning")
logging.error("Did you try to divide by zero")
logging.critical("Internet is down")
'''



'''
#Example_3:without logger formating
#This code demonstrates all the levels of logging.

# importing module
import logging
 
# Create and configure logging file
logging.basicConfig(format='%(levelname)s:%(message)s') 

# simple Test messages
print("logging in python demo_2") 
           
# log messages
logging.debug("Harmless debug Message")       
logging.info("Just an information")            
logging.warning("Its a Warning")
logging.error("Did you try to divide by zero")
logging.critical("Internet is down")
'''



'''
#Example_4: with datetime formating
#This code demonstrates all the levels of logging.

# importing module
import logging
 
# Create and configure logging file
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S %p') 

# simple Test messages
print("logging in python demo_2") 
           
# log messages
logging.debug("Harmless debug Message")       
logging.info("Just an information")            
logging.warning("Its a Warning")
logging.error("Did you try to divide by zero")
logging.critical("Internet is down")
'''




'''#Example_5:Python Logging Exception
import logging

logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s - %(levelname)s - %(message)s')


def perform_operation(value):
	if value < 0:
		raise ValueError("Invalid value: Value cannot be negative.")
	else:
		# Continue with normal execution
		logging.info("Operation performed successfully.")


try:
	input_value = int(input("Enter a value: "))
	perform_operation(input_value)
except ValueError as ve:
	logging.exception("Exception occurred: %s", ve)
'''


'''
#Example_6:Logging Configuration(1.Using Classes & Function[by using-Handlers])
# logging_in_pythone.py

import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')

'''


