from bar import Bar
from baz import Baz
from corge import Corge
from grault import Grault
from qux import Qux


class Foo():
    __bar: Bar
    __bazs: [Baz]
    __qux: Qux
    __corge: Corge
    __graults: [Grault]

    def __init__(self, bar: Bar):
        self.__bar = bar
        self.__bazs = []
        self.__qux = Qux()
        self.__corge = None
        self.__graults = []
        for i in range(4):
            self.__graults.append(Grault(self))


    @property
    def Bar(self) -> Bar:
        return self.__bar

    @Bar.setter
    def Bar(self, bar: Bar) -> None:
        self.__bar = bar

    def addBaz(self, baz: Baz) -> None:
        self.__bazs.append(baz)

    @property
    def Corge(self) -> Corge:
        return self.__corge

    @Corge.setter
    def Corge(self, corge: Corge) -> None:
        self.__corge = corge

    @property
    def Qux(self) -> Qux:
        return self.__qux

