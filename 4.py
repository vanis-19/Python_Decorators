def smart_wish(func):
    def inner():
        print('Hi')
    return inner    

def wish():
    print('Good Morning')

wish()    
