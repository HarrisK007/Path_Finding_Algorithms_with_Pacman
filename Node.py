
class Node:
    def __init__(self):
        self.__parent=None
        self.__loc=None
        self.__weight=None
        self.__g=0.0
        self.__f=0.0
        self.__h=0.0
    @property
    def parent(self):
        return self.__parent
    @property
    def loc(self):
        return self.__loc
    @property
    def weight(self):
        return self.__weight
    @property
    def g(self):
        return self.__g
    @property
    def h(self):
        return self.__h
    @property
    def f(self):
        return self.__f    
    @parent.setter
    def parent(self,obj):
        self.__parent=obj
    @loc.setter
    def loc(self,first):
        self.__loc=first
    @weight.setter
    def weight(self,num):
        self.__weight=num
    @g.setter
    def g(self,value):
        self.__g=value
    @h.setter
    def h(self,value):
        self.__h=value
    @f.setter
    def f(self,value):
        self.__f=value


