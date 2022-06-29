import unittest
# from pair_finder.pair_finder_static import PairFinderStatic
import pair_finder

class TestPairFinder(unittest.TestCase):

#TODO trzeba zamienić składnię unittest na pytest, bo GitHub Actions się pluje, ale udało się z package importem !!!

    def test_incorrect_sum_of_numbers(self):
        """
        Checks if input filepath is correct
        """
        sum_of_numbers = -1
        with self.assertRaises(ValueError):
            pair_finder.Finder._check_sum_of_numbers(value=sum_of_numbers)
        sum_of_numbers = 1.5
        with self.assertRaises(ValueError):
            pair_finder.Finder._check_sum_of_numbers(value=sum_of_numbers)

    def test_incorrect_input_filepath(self):
        """
        Checks if input filepath is correct
        """
        filepath = 12
        with self.assertRaises(ValueError):
            pair_finder.Finder._check_input_file_path(path=filepath)

    def test_incorrect_output_filepath(self):
        """
        Checks if input filepath is correct
        """
        filepath = 12
        with self.assertRaises(ValueError):
            pair_finder.Finder._check_output_file_path(path=filepath)

    def test_read_string_from_file(self):
        """
        Checks if string is read from file correctly
        """
        filepath = 'fixtures/for_test_read_string_from_file.txt'  # content: [1, 2, 3, 4, 5]
        with open(filepath, 'r') as input_stream:
            content = input_stream.read()
        self.assertEqual(content, '[1, 2, 3, 4, 5]')

    def test_read_numbers_from_string(self):
        """
        Checks if integer numbers are read correctly
        """
        data = ['4', '3', '00', '01', ]
        results = [pair_finder.Finder._read_number(number, 12) for number in data]
        [self.assertIsInstance(number, int) for number in results]

    def test_read_numbers_catch_value_error(self):
        """
        Checks if value errors are caught correctly
        """
        data = ['4.5', '-3', '33', 'DATUMO', 'Kacper']
        for number in data:
            with self.assertRaises(ValueError):
                pair_finder.Finder._read_number(number, 12)

    def test_write_string_to_file(self):
        """
        Checks if string is written to file correctly
        """
        filepath = 'outputs/for_test_write_string_to_file.txt'
        content = '[1, 12], [3, 9], '
        with open(filepath, 'w') as output_stream:
            output_stream.write(content)
        self.assertEqual(content, '[1, 12], [3, 9], ')

    def test_count_offset(self):
        """
        Checks if offset is counted correctly
        """
        sum_of_numbers = 12
        offset_list = [0] * (int(sum_of_numbers / 2) + 1)
        data = [0, 0, 1, 2, 8, 8, 9, 6, 6, 6, 10]
        filepath = 'outputs/for_test_count_offset.txt'

        with open(filepath, 'w') as output_stream:
            [pair_finder.Finder._count_offset_and_write_pair(
                number, sum_of_numbers, offset_list, output_stream) for number in data]

        self.assertEqual(offset_list, [2, 1, 0, -1, -2, 0, 1])


if __name__ == '__main__':
    unittest.main()
