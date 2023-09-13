#object  oriented programming(making  class and calling it by objects we can make varable and functions in classs)
class MoonClass:
    a=12
    def sum(self):
        print(5+4)
moonobject=MoonClass()
print(moonobject.a)
moonobject.sum();
#method and constructer
class SaqibMoon:
    b=12
    def __init__(self):#constructer no need to call
        print("welcome dream acadmy")
    def hassn(self):
        self.c=self.b*self.b
        print(self.c)
    def sum(self,a,b):
        print(a+b)

obj=SaqibMoon()
obj.hassn()
obj.sum(34,34)
#inheritance in python
#single inheritance
class A():
    def displayA(self):
        print("welcome to moons era A")
class B(A):
    def displayB(self):
        print("welcome to moons era B")
obj=B()
obj.displayA()
obj.displayB()
#multilable inheritance
class A():
    def displayA(self):
        print("welcome to moons era A")
class B(A):
    def displayB(self):
        print("welcome to moons era B")
class C(B):
    def displayC(self):
        print("welcome to moon era C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
#multiple inheritance
class A():
    def displayA(self):
        print("welcome to moons era A")
class B():
    def displayB(self):
        print("welcome to moons era B")
class C(A,B):
    def displayC(self):
        print("welcome to moon era C")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
#encapsulation(making private variable and way to use it)
class Student():
    __name="saqib"#this is private variable by using double underscore
    def __init__(self):
        print(self.__name)
obj=Student()
#over loading
class Ws:
    def display(self,name=""):
        print("welcome to ws cube tech"+name)
obj=Ws()
obj.display("saqib")
#overriding
class Ws:
    def Moon(self):
        print("will you hate me")
class Rs(Ws):
    def Moon(self):
        super().Moon()
        print("will you marry  me")
obj=Rs()
obj.Moon()
obj.Moon()
