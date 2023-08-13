
def translateXYZtoABC(letter):
    if(letter == "X"):
        return "A"
    elif(letter == "Y"):
        return "B"
    elif(letter == "Z"):
        return "C"

def solveForXYZ(opponent, letter):
    if(letter == "X"):
        if(opponent == "A"):
            return "C"
        elif(opponent == "B"):
            return "A"
        elif(opponent == "C"):
            return "B"
    elif(letter == "Y"):
        if(opponent == "A"):
            return "A"
        elif(opponent == "B"):
            return "B"
        elif(opponent == "C"):
            return "C"
    elif(letter == "Z"):
        if(opponent == "A"):
            return "B"
        elif(opponent == "B"):
            return "C"
        elif(opponent == "C"):
            return "A"


def calculatePoints(match):
    if(match[0] == "A"):
        if(match[1] == "A"):
            return 1+3
        elif(match[1] == "B"):
            return 2+6
        elif(match[1] == "C"):
            return 3+0
    elif(match[0] == "B"):
        if(match[1] == "A"):
            return 1+0
        elif(match[1] == "B"):
            return 2+3
        elif(match[1] == "C"):
            return 3+6
    elif(match[0] == "C"):
        if(match[1] == "A"):
            return 1+6
        elif(match[1] == "B"):
            return 2+0
        elif(match[1] == "C"):
            return 3+3

with open('input', 'r') as input:
    total = 0
    for line in input:
        line = line.split(" ")
        total += calculatePoints((line[0], translateXYZtoABC(line[1][0])))
    print("with the naiive method: " + str(total))


with open('input', 'r') as input:
    total = 0
    for line in input:
        line = line.split(" ")
        total += calculatePoints((line[0], solveForXYZ(line[0],line[1][0])))
    print("with the real method: " + str(total))
