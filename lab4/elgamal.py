def generateBigOddNumber():
    import random
    return (2 * random.randint(2 ** 8, 2 ** 10)) + 1
def isPrime(x):
    import math
    if x % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(x)), 2):
        if x % i == 0:
            return False
    return True
def generateBigPrimeNumber():
    bigOdd = generateBigOddNumber()
    while not (isPrime(bigOdd)):
        bigOdd -= 2
    return bigOdd
def primes(n):
    primeFactors = set()
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primeFactors.add(d)
            n //= d
        d += 1
    if n > 1:
       primeFactors.add(n)
    return primeFactors


    return True
def generateGenerator(n):
    import random,math
    while(True):
        alpha = random.randrange(1,n)
        factors = list(primes(n-1))
        for factor in factors:
            if(pow(alpha,math.ceil(n-1/factor),n)==1):
                continue
            else:
                return alpha
def generateKeys():
    import random
    largeRandomPrime = generateBigPrimeNumber()
    print("prime " + str(largeRandomPrime))
    generator = generateGenerator(largeRandomPrime)
    print("generator " + str(generator))
    privateKey = random.randrange(1,largeRandomPrime-2)
    print("private key " + str(privateKey))
    publicPart = pow(generator,privateKey,largeRandomPrime)
    print("g^a " + str(publicPart))
    publicKey = (largeRandomPrime,generator,publicPart)
    return (publicKey,privateKey)
def encrypt(publicKey, message):
    import random
    alphabet = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    inOrder = True
    for character in message:
        if character not in alphabet:
            inOrder = False

    if(inOrder):
        textToNumber = 0
        string = ""
        i=len(message)-1
        for character in message:
            textToNumber += alphabet.index(character)*pow(27,i)
            string += str(alphabet.index(character))+"*27^"+str(i) + "\n"
            i-=1

        #print("text2Number " + str(textToNumber))
        # print(publicKey)
        k = random.randrange(1,publicKey[0]-1)
        alpha = pow(publicKey[1],k,publicKey[0])
        beta = textToNumber*pow(publicKey[2],k,publicKey[0])
        beta = beta%publicKey[0]

        return (alpha,beta)

    else: return False
def decrypt(private,cipher,p):
    import math
    alphabet = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    messageInNumbers = pow(cipher[0],p-1-private)*cipher[1]%p

    return str(alphabet[math.floor(messageInNumbers/27)]) + str(alphabet[math.floor(messageInNumbers%27)])
def generateBigOddNumber():
    import random
    return (2 * random.randint(2 ** 8, 2 ** 10)) + 1
def isPrime(x):
    import math
    if x % 2 == 0:
        return False
    for i in range(3, math.ceil(math.sqrt(x)), 2):
        if x % i == 0:
            return False
    return True
def generateBigPrimeNumber():
    bigOdd = generateBigOddNumber()
    while not (isPrime(bigOdd)):
        bigOdd -= 2
    return bigOdd
def primes(n):
    primeFactors = set()
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primeFactors.add(d)
            n //= d
        d += 1
    if n > 1:
       primeFactors.add(n)
    return primeFactors


    return True
def generateGenerator(n):
    import random,math
    while(True):
        alpha = random.randrange(1,n)
        factors = list(primes(n-1))
        for factor in factors:
            if(pow(alpha,math.ceil(n-1/factor),n)==1):
                continue
            else:
                return alpha
def generateKeys():
    import random
    largeRandomPrime = generateBigPrimeNumber()
    print("prime " + str(largeRandomPrime))
    generator = generateGenerator(largeRandomPrime)
    print("generator " + str(generator))
    privateKey = random.randrange(1,largeRandomPrime-2)
    print("private key " + str(privateKey))
    publicPart = pow(generator,privateKey,largeRandomPrime)
    print("g^a " + str(publicPart))
    publicKey = (largeRandomPrime,generator,publicPart)
    return (publicKey,privateKey)
def encrypt(publicKey, message):
    import random
    alphabet = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    inOrder = True
    for character in message:
        if character not in alphabet:
            inOrder = False

    if(inOrder):
        textToNumber = 0
        string = ""
        i=len(message)-1
        for character in message:
            textToNumber += alphabet.index(character)*pow(27,i)
            string += str(alphabet.index(character))+"*27^"+str(i) + "\n"
            i-=1

        #print("text2Number " + str(textToNumber))
        # print(publicKey)
        k = random.randrange(1,publicKey[0]-1)
        alpha = pow(publicKey[1],k,publicKey[0])
        beta = textToNumber*pow(publicKey[2],k,publicKey[0])
        beta = beta%publicKey[0]

        return (alpha,beta)

    else: return False
def decrypt(private,cipher,p):
    import math
    alphabet = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    messageInNumbers = pow(cipher[0],p-1-private)*cipher[1]%p

    return str(alphabet[math.floor(messageInNumbers/27)]) + str(alphabet[math.floor(messageInNumbers%27)])
def test():
    print("TESTS STARTING\n")
    keys = generateKeys()
    publicKey = keys[0]
    privateKey = keys[1]
    messeges = [" ","abc", "NU MI E OK", "ABC9", "ABCD", "ABCD EFG"]
    for message in messeges:
        decryptedMessage = ""
        print("message " + message)
        chunks = [message[i:i + 2] for i in range(0, len(message), 2)]
        for chunk in chunks:
            encrypted = encrypt(publicKey, chunk)
            if (encrypted == False):
                print("ERROR: Character not in alphabet, please input only eng uppercase letters\n")
                break
            decrypted = decrypt(privateKey, encrypted, publicKey[0])
            decryptedMessage += decrypted

        print("decrypted message " + decryptedMessage + "\n")
        if (decryptedMessage == message):
            print("ENCRYPTION-DECRYPTION SUCCEDED\n")
    print("TESTS FINISHED\n")
    return
def main():

    keys = generateKeys()
    publicKey = keys[0]
    privateKey = keys[1]
    decryptedMessage = ""
    message = input("INPUT MESSAGE PLS (uppercase letters from the english alphabet\n")
    print("message " + message)
    chunks = [message[i:i+2] for i in range(0, len(message), 2)]
    for chunk in chunks:
        encrypted = encrypt(publicKey,chunk)
        if(encrypted == False):
            print("Character not in alphabet, please input only eng uppercase letters")
            break
        decrypted = decrypt(privateKey,encrypted,publicKey[0])
        decryptedMessage += decrypted

    print("decrypted message " + decryptedMessage)

    if(decryptedMessage == message):
        print("ENCRYPTION-DECRYPTION SUCCEDED")

test()
main()
