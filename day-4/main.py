def rangeContainsOther(pair):
    firstRange = pair[0]
    secondRange = pair[1]
    if(firstRange[0] >= secondRange[0] and firstRange[1] <= secondRange[1]):
        return True
    elif(secondRange[0] >= firstRange[0] and secondRange[1] <= firstRange[1]):
        return True
    else:
        return False

def rangeOverlaps(pair):
    firstRange = pair[0]
    secondRange = pair[1]
    if(firstRange[0] >= secondRange[0] and firstRange[0] <= secondRange[1]):
        return True
    elif(firstRange[1] >= secondRange[0] and firstRange[1] <= secondRange[1]):
        return True
    elif(secondRange[0] >= firstRange[0] and secondRange[0] <= firstRange[1]):
        return True
    elif(secondRange[1] >= firstRange[0] and secondRange[1] <= firstRange[1]):
        return True
    else:
        return False

def calcCompleteContainment(lines):
    total = 0
    for pair in lines:
        if rangeContainsOther(pair):
            total += 1
    return total

def calcRangeOverlap(lines):
    total = 0
    for pair in lines:
        if rangeOverlaps(pair):
            total += 1
    return total


def main():
    with open('input', 'r') as input:
        # turning the input into tuples for each elf pair and parsing the start and end numbers
        lines = [x.split(',') for x in list(map(str.strip, input.readlines()))]
        lines = [(list(map(int, x[0].split('-'))), list(map(int, x[1].split('-')))) for x in lines]
        print(calcCompleteContainment(lines))
        print(calcRangeOverlap(lines))

main()
