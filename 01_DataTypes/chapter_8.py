ingridients=["water","milk","black_tea"]
print(ingridients)
ingridients.append("sugar")
print(ingridients)
ingridients.remove("milk")
print(ingridients)


spices_options=["Ginger","Cardamon"]
chai_ingridients=["water","milk"]
chai_ingridients.extend(spices_options)
print("Chai :",chai_ingridients)
chai_ingridients.insert(2,"black_tea")
print(chai_ingridients)

last_added=chai_ingridients.pop()
print(last_added)
print(chai_ingridients)
#sort(),reverse()

sugar_levels=[1,2,3,4,5]
print(max(sugar_levels))
print(min(sugar_levels))


base_liquid=["water","milk"]
extra_flavour=["ginger"]
full_Liquid_Mix=base_liquid+extra_flavour
print(full_Liquid_Mix)

strong_brew=["balcktea","water"]*3
print(strong_brew)

