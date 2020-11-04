def gcdDivision(a, b):
    while b != 0:
        a, b = b, a % b

    return a

def phi(n):
    cardinal = 0
    for k in range(1, n + 1):
        if (gcdDivision(k, n) == 1):
            cardinal += 1

    return cardinal

def getDivisors(n):
    divisors = []
    i = 1
    while i <= n:
        if (n % i == 0):
            divisors.append(i)
        i = i + 1
    return divisors

def test1(n):
    sum = 0
    divisors = getDivisors(n)
    for item in divisors:
        sum += phi(item)

    return sum == n

def test2():
    sum = 0
    for n in range(1, 999):
        sum += (phi(n) / (pow(2, n) - 1))


    #this needed to be rounded, it did converge to 2 (it was 1.(9))
    return sum.__round__() == 2

def getMostCommon(dictNumberOccurence):
    sortedDict = sorted(dictNumberOccurence.items(), key=lambda x: x[1])
    return sortedDict[len(sortedDict)-1][0]

def plotHistogram(dictNumberOccurence):
    import matplotlib.pyplot as plt

    lists = sorted(dictNumberOccurence.items())

    x, y = zip(*lists)

    plt.plot(x, y)
    plt.ylabel('values of phi funct')
    plt.show()
    plt.show()

def run():
    value = int(input("please input the value: "))
    bound = int(input("please input the bound: "))
    dictNumberOccurence = {}
    listOfNumbersWithV = []

    for i in range(1, bound + 1):
        dictNumberOccurence[i] = 0

    for index in range(1, bound + 1):
        if (phi(index) == value):
            listOfNumbersWithV.append(index)
        dictNumberOccurence[phi(index)] = dictNumberOccurence[phi(index)] + 1

    mostCommonV = getMostCommon(dictNumberOccurence)

    plotHistogram(dictNumberOccurence)

    print("The numbers that have v as the value are: ")
    print(listOfNumbersWithV)
    print("the most common value is: " + str(mostCommonV))

    print("test1 is " + str(test1(20)))
    print("test2 is " + str(test2()))

run()
