# def pureChai(cups):
#     print (cups*10)
# total_chai=0
#not recomemeded
# def impureChai(cups):
#     global total_chai
#     total_chai+=total_chai

def pour_chai(n):
    if(n==0):
        return "All cups poured"
    return pour_chai(n-1)

chai_types=["ginger","kadak","ginger","kadak"]
strong_chai=list(filter(lambda chai:chai=="kadak",chai_types))
print(strong_chai)
    