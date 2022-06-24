
class PairFinder:
    def __init__(self, sumOfNumbers=12, inputFilePath='./input.txt', outputFilePath='./output.txt'):
        self.__sumOfNumbers = sumOfNumbers
        self.__inputFilePath = inputFilePath
        self.__outputFilePath = outputFilePath

    @property
    def sumOfNumbers(self):
        return self.__sumOfNumbers
        
    @sumOfNumbers.setter
    def sumOfNumbers(self, value):
        try:
            if type(value) != int:
                raise ValueError(f'Cannot set {value}.\nSum of numbers must be an integer.')
            if value < 0:
                raise ValueError(f'Cannot set {value}.\nSum of numbers must be a non-negative value.')
            self.__sumOfNumbers = value
        except ValueError:
            print(ValueError)

    @property
    def inputFilePath(self):
        return self.__inputFilePath

    @inputFilePath.setter
    def inputFilePath(self, path):
        try:
            if not type(path) == str:
                raise ValueError(f'Cannot set {path}.\nSum of numbers must be a string.')
            self.__inputFilePath = path
        except ValueError:
            print(ValueError)

    @property
    def outputFilePath(self):
        return self.__outputFilePath

    @outputFilePath.setter
    def outputFilePath(self, path):
        try:
            if not type(path) == str:
                raise ValueError(f'Cannot set {path}.\nSum of numbers must be a string.')
            self.__outputFilePath = path
        except ValueError:
            print(ValueError)

    def run(self):
        offsetList = [0] * (int(self.__sumOfNumbers/2)+1)
        with open(self.__inputFilePath, 'r') as inputStream:
            content = inputStream.read()
            listOfNumbers = content.split(',')
            with open(self.__outputFilePath, 'w') as outputStream:
                for number in listOfNumbers:
                    try:
                        number = int(number)  # it may raise a ValueError that it handled below
                        if type(number) != int:
                            raise ValueError(f'Found a value: {number}.\nIt is not an integer and will be omitted.\n')
                        if number < 0:
                            raise ValueError(f'Found a value: {number}.\nIt is a negative value and will be omitted.\n')
                        if number > self.__sumOfNumbers:
                            raise ValueError(f'Found a value: {number}.\n\
                            It is greater than the sum of numbers and will be omitted.\n')
                    except ValueError:
                        print(ValueError)
                        continue
                    if number == self.__sumOfNumbers/2:
                        if offsetList[number] == 1:
                            outputStream.write(f'[{number},{self.__sumOfNumbers - number}], ')
                            offsetList[number] = 0
                        else:
                            offsetList[number] = 1
                    else:
                        flag = 1
                        if number > self.__sumOfNumbers/2:
                            flag = -1
                            number = self.__sumOfNumbers - number
                        if offsetList[number]*flag < 0:
                            outputStream.write(f'[{number},{self.__sumOfNumbers - number}], ')
                        offsetList[number] = offsetList[number] + flag
