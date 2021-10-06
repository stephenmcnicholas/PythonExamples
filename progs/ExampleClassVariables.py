class ExampleClass:
    counter = 0 #class variable, created outside of class method, incl constructor
    def __init__(self, val = 1):
        self.__first = val # this is how you access an instance variable
        ExampleClass.counter += 1 # this is how you access a class variable. 


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter) #access public class variable using this dot notation
#print(example_object_1.__dict__, example_object_1._ExampleClass__counter) # this is how you would access PRIVATE class variable
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

