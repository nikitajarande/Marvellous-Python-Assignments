def findMaximum(inputValue):
    
    max = inputValue[0]

    print("Input Value is ", inputValue)

    for data in inputValue:
        if (data > max):
            max = data

    return max

def main():
    
    inputList = []

    print("Please Enter total count")
    inputCount = int(input())

    print("Please Enter list input one by one")
    for i in range(inputCount):
        inputList.append(int(input()))
    
    ret = findMaximum(inputList)

    print("Maximum no is : ", ret)

if __name__ == "__main__":
    main()