elfCalories = []

with open('input', 'r') as input:
    lines = input.read()
    lines = lines.split("\n\n")
    for elf in lines:
        calories = 0
        for item in list(map(int, elf.split())):
            calories += int(item)
        elfCalories.append(calories)

print("top elf: " + str(max(elfCalories)))

elfCalories.sort(reverse=True)
print("top three elves total is: "+ str(elfCalories[0]+elfCalories[1]+elfCalories[2]))
