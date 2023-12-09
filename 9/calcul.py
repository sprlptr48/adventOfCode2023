def convertToList(line: str):
    numList = [] # Converted numbers
    num = ""     # The string to convert to a number
    for letter in line:
        if letter.isnumeric() or letter == "-":
            num = num + letter
        else:
            numList.append(int(num))
            num = ""
    return numList

def isZero(numbers: list):
    zeroCounter = 0
    for i in numbers:
        if i == 0:
            zeroCounter += 1
    if zeroCounter == len(numbers):
        return True
    return False

def calculateDifference(numbers: list):
    newNumbers = []
    old = numbers[0]
    for num in numbers[1:]:
        newNumbers.append(num-old)
        old = num
    return newNumbers

def createTriangle(numbers: list):
    triangle = list()
    lineCount = 0
    lastList = numbers
    while not isZero(lastList):
        triangle.append([]) #List inside a list
        triangle[lineCount].append(lastList)
        lineCount += 1
        lastList = calculateDifference(lastList)
    return triangle

def extrapolateNext(historyTriangle: list):
    finalNum = 0
    for numList in historyTriangle:
        finalNum += numList[0][-1]
    return finalNum
def extrapolateFirst(triangle: list):
    finalNum = 0
    triangle = list(reversed(triangle))
    for numList in triangle:
        finalNum = numList[0][0] - finalNum
    return finalNum

def main():
    file = open("C:/Users/egece/Projects/adventOfCode/2/input", "r")
    sum = 0
    for line in file:
        numbers = convertToList(line)
        history = createTriangle(numbers)
        result = extrapolateFirst(history)
        sum += result
    print(sum)

if __name__ == "__main__":
    main()
