class Base:
    def __funcb(self):
        print("Base class")

    def ano(self):
        self.__funcb()

class Derived:
    def _funcd(self):
        print("Derived class") 

class Child(Derived,Base):
    def funcc(self):
        print("Yoo Child class")


objc = Child()

objc.ano()
objc._funcd()
objc.funcc()
