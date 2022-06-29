import unittest
import datetime as dt
import time
from random import randint

from pair_finder.pair_finder_static import PairFinderStatic
from pair_finder.pair_finder import PairFinder
from pair_finder.pair_finder_static_alternative_algorythm import PairFinderStaticAlternativeAlgorythm


class TestPairFinder(unittest.TestCase):

    def test_large_input_many_iterations(self):
        """
        Checks whole program, namely if pairs are found and written correctly based on inout file
        """
        sum_of_numbers = 12
        input_length = 10000
        input = str([randint(0, sum_of_numbers) for _ in range(input_length)])
        input_file = 'fixtures/for_test_static_vs_instance.txt'
        output_file = 'outputs/for_test_static_vs_instance.txt'
        number_of_iterations = 1000

        with open(input_file, 'w') as output_stream:
            output_stream.write(input)

        start = time.time()
        [PairFinderStatic.run(input_file_path=input_file, output_file_path=output_file) for _ in range(
            number_of_iterations)]
        # between_1 = time.time()
        # instance_1 = PairFinder(input_file_path=input_file, output_file_path=output_file)
        # [instance_1.run() for _ in range(number_of_iterations)]
        # between_2 = time.time()
        # [PairFinderStaticAlternativeAlgorythm.run(
        #     input_file_path=input_file, output_file_path=output_file) for _ in range(number_of_iterations)]
        end = time.time()

        static_time = end - start
        # instance_time = between_2 - between_1
        # alternative_time = end - between_2
        print(f'Static time: {static_time}')
        # print(f'Instance time: {instance_time}')
        # print(f'Alternative time: {alternative_time}')

# TODO check if static class is faster or not


if __name__ == '__main__':
    unittest.main()
