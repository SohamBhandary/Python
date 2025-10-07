class Chai:
    temp="hot"
    stength="med"
cuttinng=Chai()

print(cuttinng.stength)
cuttinng.stength="hard"
print(cuttinng.stength)
print(Chai.stength)

del cuttinng.stength
print(cuttinng.stength)
