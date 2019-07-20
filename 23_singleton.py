class Dog(object):
    __instance = None
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

dog1 = Dog()
dog2 = Dog()
print(id(dog1))
print(id(dog2))
