#
def inner():
    print("I'm inner-function")
    
def outer(fn):
    fn()
    
outer(inner)

animals = ["ferret", "vole", "dog", "gecko"]

print(sorted(animals))