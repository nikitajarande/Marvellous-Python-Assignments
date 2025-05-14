def checkPrimeNumber(value):
    if(value <= 1) or ((value % 2 == 0) and value > 2):
        print(value, " Not a Prime Number")
        return
    
    for i in range(2, int((value/2)+1)):
        if value % i == 0:
            print(value , " Not a Prime Number")
            return

    print(value," It is a Prime Number")
    return

checkPrimeNumber(5)
checkPrimeNumber(7)
checkPrimeNumber(13)
checkPrimeNumber(100)
checkPrimeNumber(3)
checkPrimeNumber(1)
checkPrimeNumber(2)
checkPrimeNumber(12)
    