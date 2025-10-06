flavours=["Ginger","out of stock","lemon","discontinued","Tulsi"]

for i in flavours:
    print("items are :",i)
    if i == "out of stock":
        continue
    if i == "discontinued":
        break
    
print("Discontuined item found")
        