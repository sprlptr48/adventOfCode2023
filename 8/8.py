import io

def findNextNode(nextDirection: str, currentNode: str, path: str):
    file = open(path, "r")
    nextNode = ""
    for line in file:
        if currentNode == line[0:3]:
            if nextDirection == "L":
                nextNode = str(line[7:10])
            if nextDirection == "R":
                nextNode = str(line[12:15])
    file.close()
    return nextNode
def calculateNodes(path: str):
    totalSteps = 0
    i = 0
    route = str()
    file = open(path, "r")
    for line in file:
        route = line
        break
    file.close()
    currentNode = "AAA" # It says start at AAA
    while currentNode != "ZZZ":
        if not route[i].isalpha() or route[i] == '\n': # The spec says if there is more, go back to start
            i = 0
        currentNode = findNextNode(route[i], currentNode, path)
        i += 1
        totalSteps += 1
    return totalSteps

def main():
    path = "C:/Users/egece/Projects/adventOfCode/8/input"
    steps = calculateNodes(path)
    print(steps)

if __name__ == "__main__":
    main()