class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0: # if val is ODD
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1) # val is ODD, so a will be set to 1, b won't be set
print(example_object.a)

if hasattr(example_object, 'b'): # checks if example_object has attribute 'b'
    print(example_object.b)


class AnotherExampleClass:
    a = 1 # class variable
    def __init__(self):
        self.b = 2 # instance variable


example_object = AnotherExampleClass()

print(hasattr(example_object, 'b')) # True, instance variable b
print(hasattr(example_object, 'a')) # True, instance inherits variable a
print(hasattr(AnotherExampleClass, 'b')) # false, variable only set when object created by constructor
print(hasattr(AnotherExampleClass, 'a')) # true, class variable a


    

