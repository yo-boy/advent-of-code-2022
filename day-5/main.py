def readInputintoStacks(fileName):
    with open(fileName, 'r') as input:
        head = [x.strip("\n") for x in [next(input) for _ in range(8)]]
        parsedArray = []
        for i in range(len(head)):
            parsedLine = []
            for j in range(1, len(head[i]), 4):
                parsedLine.append(head[i][j])
            parsedArray.append(parsedLine)
        stackList = []
        for i in range(0, 8):
            letterStack = []
            for chars in parsedArray:
                if chars[i].isalpha():
                    letterStack.append(chars[i])
            stackList.append(letterStack)
        return stackList






def main():
    letterStacks = readInputintoStacks('input')
    print(letterStacks)

main()
