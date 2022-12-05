from icorge import ICorge
from ifoo import IFoo


class Corge(ICorge):
    __foo: IFoo

    def __init__(self, foo: IFoo):
        self.__foo = foo
