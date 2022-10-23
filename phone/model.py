from __future__ import annotations
from functools import total_ordering



@total_ordering
class Mobiltelefon:

    gyarto: str
    __tipus: str
    __ev: int

    def __init__(self, gyarto: str, tipus: str , ev: int = 2022) -> None:
        self.gyarto = gyarto
        self.__tipus = tipus
        self.__ev = ev

    def __repr__(self) -> str:
        return f"{self.gyarto}, {self.__tipus}, {self.__ev}"

    def __str__(self) -> str:
        return f"{self.gyarto} // {self.__tipus} ({self.__ev})"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Mobiltelefon) and \
                   (self.gyarto, self.__tipus, self.__ev) == (o.gyarto, o.__tipus, o.__ev)

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Mobiltelefon):
            return NotImplemented
        return (self.gyarto, -self.__ev, self.__tipus) < (o.gyarto, -o.__ev, o.__tipus)

    @property
    def tipus(self) -> str:
        return self.__tipus

    @tipus.setter
    def tipus(self, value:str) -> None:
        self.__tipus = value

    @property
    def ev(self) -> int:
        return self.__ev

    @ev.setter
    def ev(self, value: int) -> None:
        self.__ev = value


    @staticmethod
    def hello(telefon: list[Mobiltelefon], evszam: int) -> list:
          lista = []
          for i in telefon:
              if i.__ev < evszam:
                  lista.append(i)
          return lista




class Okostelefon(Mobiltelefon):
    __felb: str

    def __init__(self, gyarto: str, tipus: str , ev: int, felb: str)-> None:
        super().__init__(gyarto,tipus,ev)
        self.__felb = felb


    def __repr__(self) -> str:
        return f"{super().__repr__()}, {self.__felb}"


    def __str__(self) -> str:
        return f"{super().__str__()}: {self.__felb}"

    @property
    def felb(self) -> str:
        return self.__felb

