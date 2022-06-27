class PairFinder:
    def __init__(self, sum_of_numbers=12, input_file_path='./txt_files/input.txt',
                 output_file_path='./txt_files/output.txt'):
        self.__sumOfNumbers = sum_of_numbers
        self.__inputFilePath = input_file_path
        self.__outputFilePath = output_file_path

    @property
    def sum_of_numbers(self):
        return self.__sumOfNumbers

    @sum_of_numbers.setter
    def sum_of_numbers(self, value):
        try:
            if type(value) != int:
                raise ValueError(f'Cannot set {value}.\nSum of numbers must be an integer.')
            if value < 0:
                raise ValueError(f'Cannot set {value}.\nSum of numbers must be a non-negative value.')
            self.__sumOfNumbers = value
        except ValueError as e:
            print(f'ValueError: {e}')

    @property
    def input_file_path(self):
        return self.__inputFilePath

    @input_file_path.setter
    def input_file_path(self, path):
        try:
            if not type(path) == str:
                raise ValueError(f'Cannot set {path}.\nSum of numbers must be a string.')
            self.__inputFilePath = path
        except ValueError as e:
            print(f'ValueError: {e}')

    @property
    def output_file_path(self):
        return self.__outputFilePath

    @output_file_path.setter
    def output_file_path(self, path):
        try:
            if not type(path) == str:
                raise ValueError(f'Cannot set {path}. Sum of numbers must be a string.')
            self.__outputFilePath = path
        except ValueError as e:
            print(f'ValueError: {e}')

    def read_number(self, number):
        number = int(number.strip('[]() '))  # it may raise a ValueError that is handled below
        if number < 0:
            raise ValueError(f'Found a value: {number}. It is a negative value.')
        if number > self.__sumOfNumbers:
            raise ValueError(f'Found a value: {number}. It is greater than the sum of numbers.')
        return number

    def count_offset_and_write_pair(self, number, offset_list, output_stream):
        if number == self.__sumOfNumbers / 2:
            if offset_list[number] == 1:
                output_stream.write(f'[{number},{self.__sumOfNumbers - number}], ')
                offset_list[number] = 0
            else:
                offset_list[number] = 1
        else:
            flag = 1
            if number > self.__sumOfNumbers / 2:
                flag = -1
                number = self.__sumOfNumbers - number
            if offset_list[number] * flag < 0:
                output_stream.write(f'[{number},{self.__sumOfNumbers - number}], ')
            offset_list[number] = offset_list[number] + flag

    def run(self):
        offset_list = [0] * (int(self.__sumOfNumbers / 2) + 1)
        with open(self.__inputFilePath, 'r') as inputStream:
            content = inputStream.read()
            list_of_numbers = content.split(',')
            with open(self.__outputFilePath, 'w') as outputStream:
                for number in list_of_numbers:
                    try:
                        number = self.read_number(number)
                    except ValueError as e:
                        print(f'ValueError. {e} It will be omitted.')
                        continue
                    self.count_offset_and_write_pair(number, offset_list, outputStream)
