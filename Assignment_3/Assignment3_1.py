def addListMembers(inputValue):
    result = 0
    for data in inputValue:
        result = result + data

    return result

def main():
    
    inputList = []

    print("Please Enter total count")
    inputCount = int(input())

    print("Please Enter list input one by one")
    for i in range(inputCount):
        inputList.append(int(input()))
    
    ret = addListMembers(inputList)

    print("Sum of list members is : ", ret)

if __name__ == "__main__":
    main()