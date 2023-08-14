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

def main():
    with open('input', 'r') as input:
        lines = list(map(str.strip, input.readlines()))
        rucksacks = []
        for pack in lines:
            rucksacks.append((pack[:len(pack)//2],pack[len(pack)//2:]))
        total = 0
        for rucksack in rucksacks:
            total += getPriority(findDupe(rucksack))
        print(total)

main()
