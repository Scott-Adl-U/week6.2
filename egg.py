class Egg:
    def __init__(self):
        self.__type = None

    def set_type(self, eggType):
        if isinstance(eggType, str):
            self.__type = eggType
        else:
            raise TypeError("Egg type must be string!")
    
    def get_type(self):
        return self.__type
    
    egg = property(get_type, set_type)