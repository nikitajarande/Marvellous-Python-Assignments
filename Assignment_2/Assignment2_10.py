
def addDigits(value):
    output = 0

    while value > 0:
        no = int(value%10)
        output += no
        value = int(value / 10)
    
    return output

ret = addDigits(5187934)
print("Digits are", ret)

ret = addDigits(0)
print("Digits are", ret)
