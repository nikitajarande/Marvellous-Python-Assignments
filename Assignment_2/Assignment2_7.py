def printNumber(value):
     for i in range(value, 0, -1):  
        for j in range(1, value+1):
            print(j, end = "  ")
        print("")

printNumber(5)