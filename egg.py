
class Egg:
    def __init__(self, eggType):
        self.__type = eggType

    def set_type(self, eggType):
        if isinstance(eggType, str):
            self.__type = eggType
        else:
            raise TypeError("Egg type must be string!")
    
    def get_type(self):
        return self.__type
    
    name = property(get_type, set_type)
    
    def hatch(self):
        return self.__type()

