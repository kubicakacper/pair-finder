class PairFinderStatic:

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

    @classmethod
    def read_number(cls, number, sum_of_numbers):
        number = int(number.strip('[]() '))  # it may raise a ValueError that is handled below
        if number < 0:
            raise ValueError(f'Found a value: {number}. It is a negative value.')
        if number > sum_of_numbers:
            raise ValueError(f'Found a value: {number}. It is greater than the sum of numbers.')
        return number

    @classmethod
    def count_offset_and_write_pair(cls, number, sum_of_numbers, offset_list, output_stream):
        if number == sum_of_numbers / 2:
            if offset_list[number] == 1:
                output_stream.write(f'[{number},{sum_of_numbers - number}], ')
                offset_list[number] = 0
            else:
                offset_list[number] = 1
        else:
            flag = 1
            if number > sum_of_numbers / 2:
                flag = -1
                number = sum_of_numbers - number
            if offset_list[number] * flag < 0:
                output_stream.write(f'[{number},{sum_of_numbers - number}], ')
            offset_list[number] = offset_list[number] + flag

    @classmethod
    def run(cls, input_file_path='./txt_files/input.txt', output_file_path='./txt_files/output.txt', sum_of_numbers=12):
        cls.check_sum_of_numbers(sum_of_numbers)
        cls.check_input_file_path(input_file_path)
        cls.check_output_file_path(output_file_path)
        offset_list = [0] * (int(sum_of_numbers / 2) + 1)
        with open(input_file_path, 'r') as input_stream:
            content = input_stream.read()
            list_of_numbers = content.split(',')
            with open(output_file_path, 'w') as output_stream:
                for number in list_of_numbers:
                    try:
                        number = cls.read_number(number, sum_of_numbers)
                    except ValueError as e:
                        print(f'ValueError. {e} It will be omitted.')
                        continue
                    cls.count_offset_and_write_pair(number, sum_of_numbers, offset_list, output_stream)
