def countDigits(value):
    output = 0

    if value == 0:
        return 1
    
    while value > 0:
        output += 1
        value = int(value / 10)
    
    return output

ret = countDigits(5187934)
print("Digits are", ret)

ret = countDigits(0)
print("Digits are", ret)
