from ebaz import EBaz
from grault import Grault
from ibar import IBar
from icorge import ICorge
from ifoo import IFoo
from iqux import IQux
from qux import Qux


class Foo(IFoo):
    __bar: IBar
    __bazs: [EBaz]
    __qux: IQux
    __corge: ICorge
    __graults: [Grault]

    def __init__(self, bar: IBar):
        self.__bar = bar
        self.__bazs = []
        self.__qux = Qux()
        self.__corge = None
        self.__graults = []
        for i in range(4):
            self.__graults.append(Grault(self))

    @property
    def Bar(self) -> IBar:
        return self.__bar

    @Bar.setter
    def Bar(self, bar: IBar) -> None:
        self.__bar = bar

    def addBaz(self, baz: EBaz) -> None:
        self.__bazs.append(baz)

    @property
    def Corge(self) -> ICorge:
        return self.__corge

    @Corge.setter
    def Corge(self, corge: ICorge) -> None:
        self.__corge = corge

    @property
    def Qux(self) -> IQux:
        return self.__qux
