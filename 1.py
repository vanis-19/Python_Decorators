def outer_div(func):  
    def inner(x,y):  
        if(x<y):  
            x,y = y,x  
            func(x,y)  
    return inner


@outer_div
def divide(x,y):  
    print(x//y) 


divide(2,4)    














'''In Decorators, functions are passed as an argument into another function and then called
 inside the wrapper function'''

