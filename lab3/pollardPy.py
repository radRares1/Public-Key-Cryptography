def gcdDivision(a, b):
    while b != 0:
        a, b = b, a % b

    return a
def createPolynomial(coefficientList, x):
    result = 0
    for index in range(0, len(coefficientList)):
        result = result + coefficientList[index] * pow(x, len(coefficientList) - index - 1)

    return result
def pollardRho(x0, n, coefficientList=[1, 0, 1]):
    sequenceContainer = [x0]

    lastX0 = x0
    for index in range(1, 500):
        currentX0 = createPolynomial(coefficientList, lastX0) % n
        sequenceContainer.append(currentX0)
        lastX0 = currentX0

    for index in range(1, 250):
        print("j = " + str(index))
        print("x2_j = " + str(sequenceContainer[2 * index]))
        print("x_j = " + str(sequenceContainer[index]))

        absoluteDifference = abs(sequenceContainer[2 * index] - sequenceContainer[index])
        print("|x2_j - x_j| = " + str(absoluteDifference))

        d = gcdDivision(absoluteDifference, n)
        print("d = " + str(d))
        if ((1 < d) and (d < n)):
            print(str(d) + " is a non-trivial factor of n")
            return str(d)
        elif (d == n):
            print("STOP AND FAILURE")
            return "STOP AND FAILURE"
        else:
            continue
def mapFunct(element):
    return int(element)
def gcdDivision(a, b):
    while b != 0:
        a, b = b, a % b

    return a
def createPolynomial(coefficientList, x):
    result = 0
    for index in range(0, len(coefficientList)):
        result = result + coefficientList[index] * pow(x, len(coefficientList) - index - 1)

    return result
def pollardRho(x0, n, coefficientList=[1, 0, 1]):
    sequenceContainer = [x0]

    lastX0 = x0
    for index in range(1, 500):
        currentX0 = createPolynomial(coefficientList, lastX0) % n
        sequenceContainer.append(currentX0)
        lastX0 = currentX0

    for index in range(1, 250):
        print("j = " + str(index))
        print("x2_j = " + str(sequenceContainer[2 * index]))
        print("x_j = " + str(sequenceContainer[index]))

        absoluteDifference = abs(sequenceContainer[2 * index] - sequenceContainer[index])
        print("|x2_j - x_j| = " + str(absoluteDifference))

        d = gcdDivision(absoluteDifference, n)
        print("d = " + str(d))
        if ((1 < d) and (d < n)):
            print(str(d) + " is a non-trivial factor of n")
            return str(d)
        elif (d == n):
            print("STOP AND FAILURE")
            return "STOP AND FAILURE"
        else:
            continue
def generatePolys(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n - r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i + 1:] + indices[i:i + 1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
def test():
    #list of a negative int, small prime, product of two primes
    numbers = [-124,587,58829]
    allDegreeThree = set(generatePolys([1,0,1,0,1], 3))
    times = []
    import time

    for n in numbers:
        for coef in allDegreeThree:
            start_time = time.time()
            for x0 in range(2, 500):
                result = pollardRho(x0, n, coef)
                if (result != "STOP AND FAILURE"):
                    break
                else:
                    continue
            times.append((time.time() - start_time,str(n),str(coef),result))

    for item in times:
        print(" it took --- %s seconds to run pollard rho for number %s with poly %s and result %s"
              % (item[0],item[1],item[2],item[3]))

def main():
    custom = input("Do you want a custom polynomial?(y/n) \n**the default is x^2 + 1\n")
    if (custom == "y"):

        coeficients = input("Plase input the coefficients separated"
                            " by commas (i.e 1,0,1 is x^2 + 1)\n")
        coeficients = list(map(mapFunct, coeficients.split(",")))

        n = int(input("Please input the n you want to factorize\n"))

        for x0 in range(2, 500):
            result = pollardRho(x0, n, coeficients)
            if (result != "STOP AND FAILURE"):
                return result
            else:
                continue

    elif (custom == "n"):

        n = int(input("Please input the n you want to factorize\n"))

        for x0 in range(2, 500):
            if (pollardRho(x0, n) == True):
                break
            else:
                continue

    else:
        print("re-run and please answer with y/n only, thank you ^-^\n")
test()
main()
