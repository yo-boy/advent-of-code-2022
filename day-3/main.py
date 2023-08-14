def getPriority(item):
    if item.isupper():
        return(ord(item)-38)
    else:
        return(ord(item)-96)

def findDupe(rucksack):
    firstCompartment = rucksack[0]
    secondCompartment = rucksack[1]
    for firstItem in firstCompartment:
        for secondItem in secondCompartment:
            if firstItem == secondItem:
                return firstItem

def checkAllRucksackPriority(rucksacks):
        total = 0
        for rucksack in rucksacks:
            total += getPriority(findDupe(rucksack))
        return total


def returnBadge(group):
    for firstElf in group[0]:
        for secondElf in group[1]:
            for thirdElf in group[2]:
                if (firstElf == secondElf == thirdElf):
                    return firstElf

def checkAllGroupPriority(elfGroups):
    total = 0
    for group in elfGroups:
        total += getPriority(returnBadge(group))
    return total

def main():
    with open('input', 'r') as input:
        lines = list(map(str.strip, input.readlines()))
        rucksacks = []
        for pack in lines:
            rucksacks.append((pack[:len(pack)//2],pack[len(pack)//2:]))
        print(checkAllRucksackPriority(rucksacks))
        elfGroups = []
        for i in range(0, len(lines)-1, 3):
            elfGroups.append((lines[i], lines[i+1], lines[i+2]))
        print(checkAllGroupPriority(elfGroups))

main()
