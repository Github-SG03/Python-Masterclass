#####################################MULTITHREADING_MULTIPROCESSING_IN_PYTHON########################################################
#####################################MULTITHREADING#############################################################################
#How to achieve multithreading in Python[To achieve multithreading, we need to import the threading module in Python Program & ways to define thread class as:]



#Example_1.1:creating thread without using any class
import threading                                                   #1..executed by main thread [A threading module is made up of a Thread class, which is instantiated to create a Python thread object.]
def print_hello(n):                                                #2.executed by main thread /5.these is executed by child thread
 print("Hello, how old are you ", n)
 print("this thread is executed by", threading.current_thread())
t1 = threading.Thread( target = print_hello, args =(18, ))         #3..executed by main thread [here target='print_hello' is function name executed by the thread & 'args' is the argument passed to the function]
t1.start()  # starting the thread t1                               #4..executed by main thread 
for i in range(5):                                                 #6.these is executed by the main thread
 print("main thread")
 



#Example_1.2:creating thread by extending thraed class
from threading import *                                                                                      #1.executed by main thread 
class MyThread(Thread):                                                                                      #2.ignored by main thread/#5.executed by child thread 
    def run(self):#here 'run()' is thread class method [used to define a thread's activity and can be overridden by a class that extends the threads class.]
       print("child thread")

t1=MyThread()                                                                                                 #3.executed by main thread       
t1.start()#here'start()'is thread class method[to start the execution of thread class activity]               #4.executed by main thread 
for i in range(10):                                                                                           #6.executed by main thread 
    print("main thread")





#Example_1.3:creating thread by without extending thraed class
from threading import *                   #1.executed by main thread 
class Test:                               #2.ignored by main thread/6.executed by child thread 
    def m1(self):
        for i in range(10):
            print("child thread")

obj=Test()                                #3.executed by main thread 
t1=Thread(target=obj.m1())                #4.executed by main thread 
t1.start()                                #5.executed by main thread 
for i in range(10):                       #7.executed by main thread 
    print("main thread")
 



#################################################################################################################################################################################################################################################################################################################################################################################
 
#Synchronizing Threads in Python using 'join()':It is a thread synchronization mechanism that ensures no two threads can simultaneously execute a particular segment inside the program to access the shared resources. The situation may be termed as critical sections. We use a race condition to avoid the critical section condition
#'join()': this method used in the thread class to halt the main thread's execution and waits till the complete execution of the child thread object. When the thread object is completed, it starts the execution of the main thread in Python.

#Example_1
import time  
import threading  
from threading import *  
def cal_sqre(num): # define a square calculating function  
 print(" Calculate the square root of the given number")  
 for n in num: # Use for loop   
  time.sleep(0.3) # at each iteration it waits for 0.3 time 
  print("Square of",n ,"is :", n * n)  
 
def cal_cube(num): # define a cube calculating function  
 print(" Calculate the cube of  the given number")  
 for n in num: # for loop  
  time.sleep(0.3) # at each iteration it waits for 0.3 time  
  print(" Cube of ",n ,"is: ", n * n *n)  

ar = [4, 5, 6, 7, 2] # given array    
t = time.time() # get total time to execute the functions  
#cal_cube(ar)  
#cal_sqre(ar)  
# Create two threads
th1 = threading.Thread(target=cal_sqre, args=(ar, ))  
th2 = threading.Thread(target=cal_cube, args=(ar, )) 
# Start the threads 
th1.start()  
th2.start() 
print("list of running thread is:",threading.enumerate(),"& numberv of running thread is",threading.active_count())
print("native_id of thread 1:",get_native_id())
if th1.is_alive():
    print("Task 1 is still alive") 
if th2.is_alive():
    print("Task 1 is still alive")
# Wait for the threads to finish[we can also use th1.join(5) & th2.join(5) this implies The join() method is used to wait for both threads to finish after they start executing simultaneously, with a timeout of 5 seconds. If either thread does not finish within 5 seconds, the join() method will return and the calling thread will continue execution.]
th1.join(5)  
th2.join(5)  
print(" Total time taking by threads is :", time.time() - t) # print the total time  
print(" Again executing the main thread:",threading.main_thread())  
print(" Thread 1:",th1.name, "and Thread 2:",th2.name, "have finished their execution.") 
if th1.is_alive():
    print("Task 1 is still alive") 
else:
    print("Task 1 is dead")
if th2.is_alive():
    print("Task 1 is still alive")
else:
    print("Task 1 is dead")







