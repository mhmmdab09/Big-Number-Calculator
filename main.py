def recieveNumber():
    inputNumber = input("enter number : ")
    num = []
    for digit in inputNumber:
        num.append(int(digit))
    return num

def outNumber(num):
    if num[0] == 0:
        del num[0]
    print("output is: ", end='')
    for i in num:
        print(i, end='')
    print()

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
    carry = False

    for n in range(len(maxLen)):
        outNum.append(maxLen[n])
        outNum[n] += minLen[n]
        if carry == True:
            outNum[n] += 1
            carry = False
        if outNum[n] > 9:
            outNum[n] -= 10
            carry = True

    if carry == True :
        outNum.append(1)
            
    
    return reverseNumber(outNum)

outNumber(addNumbers(recieveNumber(), recieveNumber()))