from MarvellousNum import checkPrimeNumber

def addPrimeNumber(inputValue):
    sum = 0
    for data in inputValue:
        if (checkPrimeNumber(data) == True):
            print("Prime no. is : ", data)
            sum += data

    return sum

def main():
    
    inputList = []

    print("Please Enter total count")
    inputCount = int(input())

    print("Please Enter list input one by one")
    for i in range(inputCount):
        inputList.append(int(input()))
    
    ret = addPrimeNumber(inputList)

    print("Addition of prime no.s are : ",ret)

if __name__ == "__main__":
    main()