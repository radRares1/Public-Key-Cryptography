def gcdSubstraction(a, b):
    while a != b:
        if (a > b):
            a = a - b
            print(a)
        else:
            b = b - a
            print(b)

    return a

def gcdDivision(a, b):
    while b != 0:
        a, b = b, a % b
        print("a = %s;"%a,"b = %s;"%b)

    return a

def gcdLoop(inputList):
    if (len(inputList) != 0):
        gcd = inputList[0]
        for i in range(1, len(inputList)):
            if gcd > inputList[i]:
                lowBound = inputList[i]
            else:
                lowBound = gcd
            for j in range(1, lowBound + 1):
                if ((gcd % j == 0) and (inputList[i] % j == 0)):
                    print("dasd")
                    currentGcd = j
                    print("current gcd =%s;" %x`currentGcd)
            gcd = currentGcd
    return gcd


print("subtraction")
print(gcdSubtraction(12,20))
print("division")
print(gcdDivision(12,20))
print("loop")
print(gcdLoop([12,20]))
