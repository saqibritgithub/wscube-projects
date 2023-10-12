class DomoClass:
    def display_info(self):
        print("helloo friends how are you")
class Ip(DomoClass):
    def display_info(self):
        super().display_info()
        print("my name is hacker")
obj=Ip()
obj.display_info()
#overloading
class Overloading:
    def display_info(self,name=""):
        print("welcome to the party"+ name)
obj=Overloading()
obj.display_info("moon")

   

