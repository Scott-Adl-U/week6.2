from dinosaur import ConcreteDinosaur, Dinosaur


class Egg:
    def __init__(self, eggType: Dinosaur):
        self.__type = eggType

    def set_type(self, eggType):
        if isinstance(eggType, str):
            self.__type = eggType
        else:
            raise TypeError("Egg type must be string!")

    def get_type(self):
        return self.__type

    name = property(get_type, set_type)


dinosaur = ConcreteDinosaur("Joe", "female", 20)
