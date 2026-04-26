from abc import ABC, abstractmethod
# Abstract class
class Dinosaur(ABC):
    def __init__(self, name:str, gender:str, age:int):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__egg = None

    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def get_age(self):
        return self.__age
    def get_egg(self):
        return self.__egg
    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        self.__name = name
    def set_gender(self, gender):
        # For the sake of this program gender is binary
        if not isinstance(gender, str):
            raise TypeError("Gender must be string value!")
        if gender not in ("male", "female"):
            raise TypeError("Gender must be 'male' or 'female' value")
        self.__gender = gender
    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError("Age must be int value!")
        self.__age = age
    
    age = property(get_age, set_age)
    name = property(get_name, set_name)
    gender = property(get_gender, set_gender)


    @abstractmethod
    def lay_egg(self):
        pass
    @abstractmethod
    def warm_egg(self):
        pass
    @abstractmethod
    def name_baby(self):
        pass

class ConcreteDinosaur(Dinosaur):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)