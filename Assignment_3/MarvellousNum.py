def checkPrimeNumber(value):
    if(value <= 1) or ((value % 2 == 0) and value > 2):
        return False
    
    for i in range(2, int((value/2)+1)):
        if value % i == 0:
            return False

    return True