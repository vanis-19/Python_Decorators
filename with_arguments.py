from deco import do_twice
@do_twice
def display(name):
    print(f"Hello {name}")


display("John")