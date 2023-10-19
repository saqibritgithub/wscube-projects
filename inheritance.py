class Employe:
    def __init__(self,name,id,address):
        self.name= name
        self.id= id
        self.address= address
    def showdetails(self):
        print(f"The id , name and address of empoloyee is{self.name} id is{self.id} address is{self.address}")
myobj=Employe("saqib moon",1234,"pindi stop")
myobj.showdetails()
#Access modifiers in python
#public
#private
#protected
class Company():
    def __init__(self,name):
        self. __name=name
a=Company("harry")
print(a.name)#not accesessed because it is private
print(a. _Company__name)#how to acsesss
class Saqib:
    def __init__(self):
        self. __name= ""
    def getter(self):
        return self.__name
    def setter(self,name):
        self.__name=name
obj=Saqib()
obj.setter("moon")
neme=obj.getter()
print(neme)

