from dinosaur import Dinosaur
from abc import ABC, abstractmethod


class Carnivore(Dinosaur, ABC):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)

    @abstractmethod
    def hunt(self):
        pass
