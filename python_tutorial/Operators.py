######### operator in python###########
# 1.Arithematic opereator
a = 4
b = 3
print("sum a&b:",a+b )
print("difference a&b:", a-b)
print("multiplication a&b:", a*b)
print("division a&b:", a/b)
print("modulous a&b:",a%b )
print("exponential a&b:",a**b )
print("floor division a&b:",a//b )

# 2.comparison  operetor
a=4
b=3
print("(a+b)==(b+4):",(a+b)==(b+4))
print("(a+b)!=b:",(a+b)!=b)
print("(a-b)>b:",(a-b)>b)
print("(a+b)<b:",(a+b)<b)
print("(a-1)>=b:",(a-1)>=b)
print("(a+1)<=b:",(a+1)<=b)

# 3.logical operetor
exp1=2>1
exp2=5<4
print("exp1 and exp2:",exp1 and exp2)
print("exp1 and exp2:",exp1 or exp2)
print("not(exp1):",not(exp1))

# 4.identity operator
x=5
y=5
print("x is y:",x is y)
print("x is not y:",x is not y)
print( [] == [] ) #empty list are same 
print( [] is [] ) #empty list are need not to be same object(same identity) as (list & dictionary) are stored independently & are mutable
print( {} == {} )  
print( {} is {} )
print( () is () )  #true as they are immutable



# 5. membership operator
fruits=['banana','apple','mango']
print("mango in fruit:","mango" in fruits)
print("apple in fruit:","apple"  not in fruits)

# 6. bitwise operator
a=10 #a=1010(in binary)
b=11 #b=1011(in binary)
print("binary(a):",bin(a),"&","binary(b):",bin(b))
print("a&b:",a&b)
print("a|b:",a|b)
print("a^b:",a^b)
print("~a:",~a)
print("a>>2",a>>2)
print("a<<2",a<<2)


#Asignment operator
a=2
b=8
a+=b #a=a+b
a-=b
a*=b
a/=b
a%=b
a**=b
a//=b
print("a+=b",a)
print("a-=b",a)
print("a*=b",a)
print("a/=b",a)
print("a%=b",a)
print("a**=b",a)
print("a//=b",a)

def the_outer_function():  
    var = 10  
    def the_inner_function():  
        nonlocal var    #nonlocal is same as global 
        var =14            #here using 'the_outer()_function' and changing its value as it will not give error as it is not global variable(local to function)
        print("The value inside the inner function: ", var)  
    the_inner_function()  
    print("The value inside the outer function: ", var)
the_outer_function()  

  
    
       






