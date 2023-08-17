def getInputStream(input):
    with open('input', 'r') as input:
        return ([*input.read().strip()])

def detectPacketStart(input):
    for i in range(3, len(input)):
        if (4 == len(set(input[i-3:i+1]))):
            return i+1

def detectMessageStart(input):
    for i in range(13, len(input)):
        if (14 == len(set(input[i-13:i+1]))):
            return i+1

def main():
    input = getInputStream('input')
    print(detectPacketStart(input))
    print(detectMessageStart(input))

main()
