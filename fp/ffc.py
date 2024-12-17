#
def inner():
    print("I'm inner-function")
    
def outer(fn):
    fn()
    
outer(inner)
