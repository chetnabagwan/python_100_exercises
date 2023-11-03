def foo(a, b)->None:
    #print(a + b)
    return (a+b)
 
x = foo(2, 3) * 10 #throw Type error as foo func returns None and we are mutliplying a integer with None.
print(x)