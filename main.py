def recieveNumber():
    inputNumbers = []
    tempIn = ""
    while True:
        num = []
        tempIn = input("Enter Number or 'end' : ")
        if tempIn == "end":
            break
        else:
            for word in tempIn:
                num.append(int(word))
        inputNumbers.append(num)
    return inputNumbers

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

def addMultiNumbers(numbers):
    def addTwoNumbers(firstNumber, secondNumber):
        if(len(firstNumber) > len(secondNumber)):
            maxLen = reverseNumber(firstNumber)
            minLen = reverseNumber(secondNumber)
        else:
            maxLen = reverseNumber(secondNumber)
            minLen = reverseNumber(firstNumber)
        for n in range(len(maxLen) - len(minLen)):
            minLen.append(0)
        outNum = []
        carry = False
        for n in range(len(maxLen)):
            outNum.append(maxLen[n])
            outNum[n] += minLen[n]
            if carry:
                outNum[n] += 1
                carry = False
            if outNum[n] > 9:
                outNum[n] -= 10
                carry = True
        if carry:
            outNum.append(1)
        return reverseNumber(outNum)
    sum = []
    for number in numbers:
        sum = addTwoNumbers(sum, number)
    return sum

def mainMenu():
    print()
    print(25 * "-")
    print("Main Menu")
    print(25 * "-")
    userInput = int(input('''Choose the operation :
    1- Sum
    2- Sub
    3- Multiply
    4- Divide
    
    0- Exit
    
    enter number of the operation you want (only intigers) : '''))
    if userInput == 1:
        outNumber(addMultiNumbers(recieveNumber()))
    elif userInput == 0:
        exit()
    elif userInput == 2:
        print("*** This function will be available in the future ***")
    elif userInput == 3:
        print("*** This function will be available in the future ***")
    elif userInput == 4:
        print("*** This function will be available in the future ***")
    else:
        print("***** wrong input *****")

while(True):
    mainMenu()