def chai_status(cupsLeft):
    if cupsLeft==0:
        return "Sorry chai over"
    return "Chai preparing"
print(chai_status(0))
print(chai_status(5))