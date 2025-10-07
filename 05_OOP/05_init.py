class Chai:
    def __init__(self,type_,size):
        self.type=type_
        self.size=size
    def summary(self):
        return self.size,self.type
order=Chai("Masala","200")
print(order.summary())
order1=Chai("Ginger","100")
print(order1.summary())

