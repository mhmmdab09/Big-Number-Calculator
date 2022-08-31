def recieveNumber():
    inputNumber = input("enter number : ")
    num = []
    for digit in inputNumber:
        num.append(int(digit))
    return num

def reverseNumber(num):
    outNum = []
    for digit in reversed(num):
        outNum.append(digit)
    return outNum


def addNumbers(firstNumber, secondNumber):
    if(len(firstNumber) > len(secondNumber)):
        maxLen = reverseNumber(firstNumber)
        minLen = reverseNumber(secondNumber)
    else:
        maxLen = reverseNumber(secondNumber)
        minLen = reverseNumber(firstNumber)
    
    for n in range(len(maxLen)):
        minLen.append(0)
    
    outNum = []

    for n in range(len(maxLen)):
        outNum.append(0)

    for n in range(len(maxLen)):
        outNum[n] += maxLen[n]
        outNum[n] += minLen[n]
        if outNum[n] > 9:
            outNum[n] -= 10
    
    return reverseNumber(outNum)

print(addNumbers(recieveNumber(), recieveNumber()))