class Chai:
    size=150
    def desc(self):
        return self.size
cup=Chai()
cu2=Chai()
print(cup.desc())
cu2.size=100
print(cu2.desc())
