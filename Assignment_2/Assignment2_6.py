def printPattern(value):
    
    for i in range(value, 0, -1):  
        for j in range(1, i+1):
            print("*", end = "  ")
        print("")

printPattern(5)