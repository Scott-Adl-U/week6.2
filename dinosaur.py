from abc import ABC, abstractmethod
from egg import Egg
# Abstract class


class Dinosaur(ABC):
    def __init__(self, name: str, gender: str, age: int):
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__egg = []
        self.__eggType = None
        self.__food_inventory = []

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def get_eggs(self):
        return list(self.__egg)

    def get_eggType(self):
        return self.__eggType

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        self.__name = name


    def set_gender(self, gender):
        # For the sake of this program gender is binary
        if not isinstance(gender, str):
            raise TypeError("Gender must be string value!")
        if gender not in ("male", "female"):
            raise ValueError("Gender must be 'male' or 'female' value")
        self.__gender = gender

    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError("Age must be int/number value!")
        self.__age = age

    def set_egg(self, egg):
        if not self.gender == "female":
            raise TypeError("Only female dinosaurs can tend to eggs!")
        if not isinstance(egg, str):
            raise TypeError("Egg must be str object!")
        if not egg == self.__eggType:
            raise TypeError(f"Egg must be {self.eggType} type!")
        self.__egg.append(Egg(egg))

    age = property(get_age, set_age)
    name = property(get_name, set_name)
    gender = property(get_gender, set_gender)
    eggType = property(get_eggType)
    eggs = property(get_eggs)

    def __str__(self):
        eggs = "None" if not self.eggs else ", ".join(
            str(e) for e in self.eggs)
        return (
            f"Name: {self.name}\n"
            f"Type: {self.__class__.__name__}\n"
            f"Gender: {self.gender}\n"
            f"Age: {self.age}\n"
            f"Eggs: {eggs}\n"
        )
    # TODO: Implement this in descendant classes before removing comments
    # @abstractmethod
    # def lay_egg(self):
        pass
    # @abstractmethod
    # def warm_egg(self):
        pass
    # @abstractmethod
    # def name_baby(self):
        pass


class ConcreteDinosaur(Dinosaur):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)


dinosaur = ConcreteDinosaur("Bill", "male", 20)
print(dinosaur)
dinosaur.gender = "female"
print(dinosaur)
