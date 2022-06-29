class PairFinderStaticAlternativeAlgorythm:

    @staticmethod
    def check_sum_of_numbers(value):
        try:
            if type(value) != int:
                raise ValueError(f'Cannot set {value}.\nSum of numbers must be an integer.')
            if value < 0:
                raise ValueError(f'Cannot set {value}.\nSum of numbers must be a non-negative value.')
        except ValueError as e:
            print(f'ValueError: {e}')

    @staticmethod
    def check_input_file_path(path):
        try:
            if not type(path) == str:
                raise ValueError(f'Cannot set {path}.\nSum of numbers must be a string.')
        except ValueError as e:
            print(f'ValueError: {e}')

    @staticmethod
    def check_output_file_path(path):
        try:
            if not type(path) == str:
                raise ValueError(f'Cannot set {path}. Sum of numbers must be a string.')
        except ValueError as e:
            print(f'ValueError: {e}')

    # @classmethod
    # def _read_number(cls, number, sum_of_numbers):
    #         number = int(number.strip('[]() '))  # it may raise a ValueError that is handled below
    #         if number < 0:
    #             raise ValueError(f'Found a value: {number}. It is a negative value.')
    #         if number > sum_of_numbers:
    #             raise ValueError(f'Found a value: {number}. It is greater than the sum of numbers.')
    #         return number

    @classmethod
    def read_numbers(cls, list_of_numbers, sum_of_numbers):
        for count, value in enumerate(list_of_numbers):
            try:
                number = int(value.strip('[](){} '))  # it may raise a ValueError that is handled below
                if number < 0:
                    raise ValueError(f'Found a value: {number}. It is a negative value.')
                if number > sum_of_numbers:
                    raise ValueError(f'Found a value: {number}. It is greater than the sum of numbers.')
                list_of_numbers[count] = number
            except ValueError as e:
                print(f'ValueError. {e} It will be omitted.')
                continue
        # list_of_numbers = [cls._read_number(value, sum_of_numbers) for count, value in enumerate(list_of_numbers)]

    @classmethod
    def count_pairs(cls, count_numbers, count_pairs, sum_of_numbers):
        for count, value in enumerate(count_pairs):
            count_pairs[count] = min(count_numbers[count], count_numbers[sum_of_numbers - count])
            if sum_of_numbers % 2 == 0:
                count_pairs[int(sum_of_numbers / 2)] = int(count_pairs[int(sum_of_numbers / 2)] / 2)

    @classmethod
    def write_pairs(cls, count_pairs, output_file_path, sum_of_numbers):
        with open(output_file_path, 'w') as output_stream:
            [output_stream.write(f'[{count},{sum_of_numbers - count}], ') for count, value in enumerate(count_pairs)]

    @classmethod
    def run(cls, input_file_path='./txt_files/input.txt', output_file_path='./txt_files/output.txt', sum_of_numbers=12):
        cls.check_sum_of_numbers(sum_of_numbers)
        cls.check_input_file_path(input_file_path)
        cls.check_output_file_path(output_file_path)
        count_numbers = [0] * (sum_of_numbers + 1)
        count_pairs = [0] * (int(sum_of_numbers / 2) + 1)
        with open(input_file_path, 'r') as input_stream:
            list_of_numbers = input_stream.read().split(',')
            cls.read_numbers(list_of_numbers, sum_of_numbers)
            #
            # try:
            #     number = cls._read_number(number, sum_of_numbers)
            # except ValueError as e:
            #     print(f'ValueError. {e} It will be omitted.')
            #     continue
            count_numbers = [count_numbers[value] + 1 for value in list_of_numbers]
            cls.count_pairs(count_numbers, count_pairs, sum_of_numbers)
            cls.write_pairs(count_pairs, output_file_path, sum_of_numbers)

# TODO unit tests !!
# TODO and check if it works fine !!!

            # with open(output_file_path, 'w') as output_stream:
            #     for number in list_of_numbers:
            #         try:
            #             number = cls._read_number(number, sum_of_numbers)
            #         except ValueError as e:
            #             print(f'ValueError. {e} It will be omitted.')
            #             continue
            #         cls._count_offset_and_write_pair(number, sum_of_numbers, offset_list, output_stream)


    # with open('./txt_files/input.txt', 'r') as inputStream:
    #     NUMBER = 12
    #     countNumbers = [0] * (NUMBER + 1)
    #     content = inputStream.read()
    #     listOfNumbers = content.split(',')
    #     for count, value in enumerate(listOfNumbers):
    #         listOfNumbers[count] = int(value)
    #
    #     for value in listOfNumbers:
    #         countNumbers[value] = countNumbers[value] + 1
    #
    #     print(countNumbers)
    #
    #     countPairs = [0] * (int(NUMBER / 2) + 1)
    #
    #     for count, value in enumerate(countPairs):
    #         countPairs[count] = min(countNumbers[count], countNumbers[NUMBER - count])
    #         if NUMBER % 2 == 0:
    #             countPairs[int(NUMBER/2)] = int(countPairs[int(NUMBER/2)]/2)
    #
    #     for count, value in enumerate(countPairs):
    #         print(f'Number of pairs {count}-{NUMBER - count}: {value}')