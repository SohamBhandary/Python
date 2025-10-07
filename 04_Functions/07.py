def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "Yes", "Low") #positional
make_chai(tea="Green", sugar="Medium", milk="No") #keywords

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()