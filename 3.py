def smart_dev(func):
    def inner(a,b):
        if b==0:
            print(a can not divide by zero')
        else:
             print(a/b)
        func(a,b)
    return inner              
                  
                  


def add(a,b):
    print(a/b)


add(2,4)    
