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
        for i in range(0, 9):
            letterStack = []
            for chars in parsedArray:
                if chars[i].isalpha():
                    letterStack.append(chars[i])
            letterStack.reverse()
            stackList.append(letterStack)
        return stackList

def getInstructions(fileName):
    with open(fileName, 'r') as input:
        instructions = input.readlines()[10:]
        instructions = [x.strip('\n').removeprefix('move ').replace(' from ', ' ').replace(' to ', ' ') for x in instructions]
        instructions = [x.split(' ') for x in instructions]
        instructions = [list( map(int,i) ) for i in instructions]
        return instructions

def applyInstructionToStack(letterStacks, instructions):
    for instruction in instructions:
        for i in range(instruction[0]):
            if letterStacks[instruction[1]-1] != []:
                letterStacks[instruction[2]-1].append(letterStacks[instruction[1]-1].pop())

def applyUpdatedInstructions(letterStacks, instructions):
    for instruction in instructions:
        operations = int(instruction[0])
        stackFrom = int(instruction[1]-1)
        stackTo = int(instruction[2]-1)
        if (operations > len(letterStacks[stackFrom])):
            operations = len(letterStacks[stackFrom])
        crates = letterStacks[stackFrom][-operations:]
        del letterStacks[stackFrom][-operations:]
        letterStacks[stackTo].extend(crates)

def getCratesOnTop(letterStacks):
    out = ''
    for stack in letterStacks:
        out += stack[-1]
    return out

def main():
    letterStacks = readInputintoStacks('input')
    instructions = getInstructions('input')
    applyInstructionToStack(letterStacks, instructions)
    print(getCratesOnTop(letterStacks))
    letterStacks = readInputintoStacks('input')
    applyUpdatedInstructions(letterStacks, instructions)
    print(getCratesOnTop(letterStacks))

main()
