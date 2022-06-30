import logging
import sys
from datetime import datetime


class PairFinderStatic:

    @staticmethod
    def _check_sum_of_numbers(value):
        if type(value) != int:
            raise ValueError(f'Cannot set {value}.\nSum of numbers must be an integer.')
        if value < 0:
            raise ValueError(f'Cannot set {value}.\nSum of numbers must be a non-negative value.')

    @staticmethod
    def _check_input_file_path(path):
        if not type(path) == str:
            raise ValueError(f'Cannot use {path} as the input filepath. It must be a string.')


    @staticmethod
    def _check_output_file_path(path):
        if not type(path) == str:
            raise ValueError(f'Cannot use {path} as the output filepath. It must be a string.')

    @classmethod
    def _read_number(cls, number, sum_of_numbers):
        number = int(number.strip('[](){} '))  # it may raise a ValueError that is handled below
        if number < 0:
            raise ValueError(f'Found a value: {number}. It is a negative value.')
        if number > sum_of_numbers:
            raise ValueError(f'Found a value: {number}. It is greater than the sum of numbers.')
        return number

    @classmethod
    def _count_offset_and_write_pair(cls, number, sum_of_numbers, offset_list, output_stream):
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
    def run(cls, input_file_path='./txt_files/input.txt', output_file_path='./txt_files/output.txt', sum_of_numbers=12,
            separator=','):
        __logger = logging.getLogger('pair_finder_app')
        logging.getLogger().setLevel(logging.INFO)
        current_timestamp = str(datetime.now()).replace(' ', '_')
        logging.basicConfig(filename=f'diagnostic_logs/diag_{current_timestamp}.log', filemode='w', format='%(asctime)s - %(levelname)s: %(message)s')
        logging.debug(f'Algorythm started.')
        try:
            cls._check_sum_of_numbers(sum_of_numbers)
            cls._check_input_file_path(input_file_path)
            cls._check_output_file_path(output_file_path)
        except ValueError as e:
            logging.critical(f'ValueError: {e} Application will be terminated.')
            return sys.exit(1)
        offset_list = [0] * (int(sum_of_numbers / 2) + 1)
        with open(input_file_path, 'r') as input_stream:
            # logging.debug(f'Input file {input_file_path} opened.')
            content = input_stream.read()
            list_of_numbers = content.split(separator)
            with open(output_file_path, 'w') as output_stream:
                # logging.debug(f'Output file {output_file_path} opened.')
                for number in list_of_numbers:
                    try:
                        number = cls._read_number(number, sum_of_numbers)
                    except ValueError as e:
                        logging.error(f'ValueError. {e} It will be omitted.')
                        continue
                    cls._count_offset_and_write_pair(number, sum_of_numbers, offset_list, output_stream)
        logging.debug(f'Algorythm finished.')
