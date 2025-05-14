def factorial(no):
    output = 1
    i = no
    while i >= 1:
        output = output*i
        i -= 1

    return output

ret = factorial(5)
print("Factorial is : ",ret)