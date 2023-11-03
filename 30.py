#Default parameter should be at the last 

#def foo(a=1, b): wrong as Non-default argument follows default argument
    #return a + b
 

def foo(b, a=1): #Correct
    return a + b
 
x = foo - 1