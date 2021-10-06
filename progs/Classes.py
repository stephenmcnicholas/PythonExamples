class Classy:
    pass


print(Classy.__name__)
print(Classy.__module__)
obj = Classy()
print(type(obj).__name__)
print(obj.__module__)
