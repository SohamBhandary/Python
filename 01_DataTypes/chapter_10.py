chai_type=dict(type="Masala",size="Large",sugar=2)
print(chai_type)
chai_recepie={}
chai_recepie["base"]="black tea"
chai_recepie["liquid"]="milk"
print(chai_recepie)
print(chai_recepie["liquid"])
del chai_recepie["liquid"]
print(chai_recepie)
print(chai_type.keys())
print(chai_type.values())
print(chai_type.items())