def checkIfDivisibleBy5(value):
    if value % 5 == 0:
        return True
    else:
        return False
    
ret = checkIfDivisibleBy5(8)
print(ret)
ret = checkIfDivisibleBy5(25)
print(ret)