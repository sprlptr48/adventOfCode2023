file = open("input", "r")
total = 0
numList = {"1":"one", "2":"two", "3":"three", "4":"four" , "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
for line in file:
    first, last = "a", "a"
    firstIndex, lastIndex = -1, -1
    firstChosen = False
    for letter in line:
        if letter.isnumeric():
            if not firstChosen:
                first = letter
                print(letter)
                firstChosen = True
                firstIndex = line.find(letter)
                last = letter
                lastIndex = line.rfind(letter)
            else:
                lastIndex = line.rfind(letter)
                last = letter
                print(letter + "a")
    #Outer loop
    for i in numList:
        indexOf = line.find(numList[i])
        if indexOf != -1:
            if indexOf < firstIndex:
                firstIndex = indexOf
                first = i
                print(numList[i])
        indexOf = line.rfind(numList[i])
        if indexOf != -1:
            if indexOf > lastIndex:
                last = i
                print(numList[i] + "a")
                lastIndex = indexOf
            elif lastIndex == -1:
                last = str(i)
                print(numList[i] + "a")
                lastIndex = indexOf
    firstChosen = False
    if last.isnumeric() is True:
        num = (int)(first + last)
    else:
        num = (int)(first + first)
    total += num
print(total)