essential_spices={"cardamon","ginger","cinamon"}
opyional_spices={"cloves","ginger","black_pepper"}

all_spices=essential_spices.union(opyional_spices)
print(all_spices)

excess_spices=essential_spices.intersection(opyional_spices)
print(excess_spices)

