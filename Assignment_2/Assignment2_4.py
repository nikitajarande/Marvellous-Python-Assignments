def addFactors(value):
    output = 0
    for i in range(1, value):
        if(value % i == 0):
            output += i

    return output

ret =  addFactors(12)
print("Output is : ", ret)

