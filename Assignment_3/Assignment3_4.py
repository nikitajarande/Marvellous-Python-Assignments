def searchNumberList(inputValue, noToSearch):
    count = 0
    for data in inputValue:
        if (data == noToSearch):
            count += 1

    return count

def main():
    
    inputList = []

    print("Please Enter total count")
    inputCount = int(input())

    print("Please Enter list input one by one")
    for i in range(inputCount):
        inputList.append(int(input()))
    
    print("Please Enter number to search")
    toSearch = int(input())

    ret = searchNumberList(inputList, toSearch)

    print(toSearch, "found for ", ret, " times")

if __name__ == "__main__":
    main()