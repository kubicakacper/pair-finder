import unittest
from pair_finder.pair_finder_static import PairFinderStatic


class TestPairFinder(unittest.TestCase):

    def test_run(self):
        """
        Checks whole program, namely if pairs are found and written correctly based on inout file
        """
        input_file = 'fixtures/for_test_run.txt'
        output_file = 'outputs/for_test_run.txt'
        PairFinderStatic.run(input_file_path=input_file, output_file_path=output_file)
        with open(output_file, 'r') as input_stream:
            content = input_stream.read()
            self.assertEqual(content, '[6,6], [0,12], [3,9], [1,11], [0,12], ')


if __name__ == '__main__':
    unittest.main()
