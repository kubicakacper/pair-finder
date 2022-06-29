import unittest
import datetime as dt
import time
from pair_finder.pair_finder_static import PairFinderStatic
from pair_finder.pair_finder import PairFinder
from pair_finder.pair_finder_static_alternative_algorythm import PairFinderStaticAlternativeAlgorythm


class TestPairFinder(unittest.TestCase):

    def test_static_vs_instance(self):
        """
        Checks whole program, namely if pairs are found and written correctly based on inout file
        """
        input_file = 'fixtures/for_test_static_vs_instance.txt'
        output_file = 'outputs/for_test_static_vs_instance.txt'
        number_of_iterations = 10

        start = time.time()
        [PairFinderStatic.run(input_file_path=input_file, output_file_path=output_file) for _ in range(
            number_of_iterations)]
        between_1 = time.time()
        instance_1 = PairFinder(input_file_path=input_file, output_file_path=output_file)
        [instance_1.run() for _ in range(number_of_iterations)]
        between_2 = time.time()
        [PairFinderStaticAlternativeAlgorythm.run(
            input_file_path=input_file, output_file_path=output_file) for _ in range(number_of_iterations)]
        end = time.time()

        static_time = between_1 - start
        instance_time = between_2 - between_1
        alternative_time = end - between_2
        print(f'Static time: {static_time}')
        print(f'Instance time: {instance_time}')
        print(f'Alternative time: {alternative_time}')

# TODO check if static class is faster or not


if __name__ == '__main__':
    unittest.main()
