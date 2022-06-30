import unittest
# from pair_finder.pair_finder_static import PairFinderStatic
import pair_finder

class TestPairFinder(unittest.TestCase):

    def test_run_12(self):
        """
        Checks whole program, namely if pairs are found and written correctly based on inout file
        """
        input_file = './tests/fixtures/for_test_run.txt'
        output_file = './tests/outputs/for_test_run.txt'
        pair_finder.Finder.run(input_file_path=input_file, output_file_path=output_file)
        with open(output_file, 'r') as input_stream:
            content = input_stream.read()
            self.assertEqual(content, '[6,6], [0,12], [3,9], [1,11], [0,12], ')

    def test_run_13(self):
        """
        Checks whole program, namely if pairs are found and written correctly based on inout file
        """
        input_file = './tests/fixtures/for_test_run.txt'
        output_file = './tests/outputs/for_test_run.txt'
        pair_finder.Finder.run(input_file_path=input_file, output_file_path=output_file, sum_of_numbers=13)
        with open(output_file, 'r') as input_stream:
            content = input_stream.read()
            self.assertEqual(content, '[3,10], [6,7], [1,12], [4,9], [0,13], ')

    def test_run_1(self):
        """
        Checks whole program, namely if pairs are found and written correctly based on inout file
        """
        input_file = './tests/fixtures/for_test_run.txt'
        output_file = './tests/outputs/for_test_run.txt'
        pair_finder.Finder.run(input_file_path=input_file, output_file_path=output_file, sum_of_numbers=1)
        with open(output_file, 'r') as input_stream:
            content = input_stream.read()
            self.assertEqual(content, '[0,1], ')

    def test_run_0(self):
        """
        Checks whole program, namely if pairs are found and written correctly based on inout file
        """
        input_file = './tests/fixtures/for_test_run.txt'
        output_file = './tests/outputs/for_test_run.txt'
        pair_finder.Finder.run(input_file_path=input_file, output_file_path=output_file, sum_of_numbers=0)
        with open(output_file, 'r') as input_stream:
            content = input_stream.read()
            self.assertEqual(content, '[0,0], ')


if __name__ == '__main__':
    unittest.main()
