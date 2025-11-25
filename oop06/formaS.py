from abc import ABC, abstractmethod
from enum import Enum

class Cor(Enum):
    VERMELHO = "Vermelho"
    AZUL = "Azul"
    VERDE = "Verde"
    AMARELO = "Amarelo"

class Forma(ABC):
    __cor:Cor

    @abstractmethod
    def area(self) -> float:
        pass 

class Circulo(Forma):
    __raio:float

    @property
    def raio(self) -> float:
        return self.__raio
    
    @_raio.setter
    def _raio(self, raio:float) -> float:
        self._raio = raio
        super().__cor = cor
    
    def area (self) -> float:
        from math import pi
        return pi * (self._raio **2)
    
    