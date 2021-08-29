import unittest
from sorting.bubble_sort import BubbleSort


class BubbleSortTestCase(unittest.TestCase):

    def setUp(self):

        self.max_length = 10
        self.data = [6, 2, [4, 3], [[[5], None], 1], 10]
        self.list = BubbleSort()

    def test_the_max_length(self):
        """ test to see if the max length raises an exception"""
        self.assertRaises(ValueError, self.list.bubble_sort, self.data, 4)

    def test_list_for_string_and_null_values(self):
        """ test to see if the output has not null and strings """
        for value in self.list.bubble_sort(self.data, 10):
            self.assertIsInstance(value, int)

    def test_for_sorting(self):
        """ test to see if algorithm sorts """
        result = self.list.bubble_sort(self.data, self.max_length)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 10])

    def test_if_output_is_list(self):
        """check if output is a list"""
        result = self.list.bubble_sort(self.data, self.max_length)
        self.assertIsInstance(result, list)

    def test_if_list_is_empty(self):
        result = self.list.bubble_sort([], self.max_length)
        self.assertListEqual(result, [])
