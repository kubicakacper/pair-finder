from random import randint

INPUT_SIZE = 50
NUMBER = 12
INPUT_FILEPATH = './input.txt'

listOfInputNumbers = [randint(0, NUMBER) for i in range(INPUT_SIZE)]

with open(INPUT_FILEPATH, 'w') as outputStream:
    inputString = str(listOfInputNumbers).strip('[]')
    outputStream.write(inputString)
    # [outputStream.write(f'{number},') for number in listOfInputNumbers]
