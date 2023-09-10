class node:
    def __init__(self, parent=None):
        self.parent = parent
        self.fileList = []
        self.size = 0
        self.children = {}

class file:
    def __init__(self, name, size):
        self.size = size
        self.name = name

def readInput(fileName):
    return([x.strip() for x in open(fileName, 'r').readlines()])

class command:
    def __init__(self, command, argument=None):
        if(command == 'c'):
            self.command = 'cd'
            self.argument = argument
        elif(command == 'l'):
            self.command = 'ls'
            self.argument = None

def parseInstruction(input):
    if input[0] == '$':
        if input[2] == 'c':
            return command('c', input[5:])
        elif input[2] == 'l':
            return command('l')

def parseInput(input, root):
    wd = root
    ls = False
    for instruction in input:
        print(instruction)
        if instruction[0] == '$':
            ls = False
        if not ls:
            instruction = parseInstruction(instruction)
            if isinstance(instruction, command):
                if(instruction.command == 'ls'):
                    ls = True
                    continue
                elif(instruction.command == 'cd'):
                    ls = False
                    if(instruction.argument == '/'):
                        wd = root
                    elif(instruction.argument == '..'):
                        if(wd != root):
                            wd = wd.parent
                    else:
                        print(isinstance(wd.children[instruction.argument], node))
                        wd = wd.children[instruction.argument]
        else:
            if(instruction[:3] == 'dir'):
                directory = node(wd)
                wd.children[instruction[4:]] = [directory]
            else:
                print(instruction)
                name, size = instruction.split(" ")
                print(type(wd))
                print(dir(wd))
                print(isinstance(wd, node))
                wd.fileList.append(file(name, size))


def main():
    input = readInput('input')
    root = node(None)
    parseInput(input, root)

main()
