class Bikeshop():
    def __init__(self,stock):
        self.stock=stock
    def displaybikes(self):
        print("Total bikes are",self.stock)
    def rentforbike(self,q):
        if q<=0:
            print("enter greater positive no")
        elif q>self.stock:
            print("enter the no less than  stock")
        else:
            print("total price",q*100)
            print("Remaining Bikes",self.stock-q)
while True:
    obj=Bikeshop(100)
    uc=int(input("""
1:Display stock
2:Request for rent
3:Exit """))
    if uc==1:
        obj.displaybikes()
    elif uc==2:
        n=int(input("enter the quantity :"))
        obj.rentforbike(n)
    else:
        break;
