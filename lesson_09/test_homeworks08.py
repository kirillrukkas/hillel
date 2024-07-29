import unittest
from homework09 import get_sum_of_list_elements, mean_of_list, get_biggest_word, get_sum_of_even_list


class TestGetSumOfListElementsFunction(unittest.TestCase):
    def test_positive_write_list_positive_numbers(self):
        lst1=["1,2,3,4", "1,2,3,4,50",  "1,2,3"]
        self.assertListEqual(get_sum_of_list_elements(lst1), [10, 60, 6])
    
    def test_positive_write_list_negative_numbers(self):
        lst1=["-1,2,-3,4", "-1,-2,-3,-4,-50",  "1,2,-3"]
        self.assertListEqual(get_sum_of_list_elements(lst1), [2, -60, 0])

    def test_negative_untransform_elem(self):
        lst1=["-1,2,-3,4", "-1,-2,-3,-4,-50",  "atata1,2,-3"]
        self.assertEqual(get_sum_of_list_elements(lst1), [2, -60, 'Не можу це зробити!'])

    def test_negative_untransform_all_elems(self):
        lst1=["-1,2,ffgg,-3,4", "-1,-2,-3,-4,-50fgfgf",  "atata1,2,-3"]
        self.assertEqual(get_sum_of_list_elements(lst1), ['Не можу це зробити!', 'Не можу це зробити!', 'Не можу це зробити!'])
    
    def test_list_of_empty_elem(self):
        lst1=["", "",  ""]
        self.assertEqual(get_sum_of_list_elements(lst1), ['Не можу це зробити!', 'Не можу це зробити!', 'Не можу це зробити!'])

    def test_empty_list(self):
        lst1=[]
        self.assertEqual(get_sum_of_list_elements(lst1), [])

class TestMeanOfListFunction(unittest.TestCase):
    def test_positive_list_of_int(self):
        lst1 = [0,1,2,6,7]
        self.assertEqual(mean_of_list(lst1), 3.2)

    def test_positive_list_of_positive_float_and_int(self):
        lst1 = [0,1,2.1,6.3,7]
        self.assertEqual(mean_of_list(lst1), 3.28)
    
    def test_positive_list_of_negative_float_and_int(self):
        lst1 = [0, -1.1, 2.1,-6.3, 7.11]
        self.assertAlmostEqual(mean_of_list(lst1), 0.362)

    def test_negative_with_all_elem_zero(self):
        lst1 = [0,0,0,0,]
        self.assertEqual(mean_of_list(lst1), 0)
    
    def test_negative_empty_list(self):
        lst1 = []
        self.assertEqual(mean_of_list(lst1), 'List is empty')


class TestGetBiggestWordFunction(unittest.TestCase):
    def test_positive_with_different_words(self):
        lst1 =["hi", "hello", "worlds", "annotations"]
        self.assertEqual(get_biggest_word(lst1), 'annotations')
    
    def test_positive_with_two_longest_words(self):
        lst1 =["hi", "hello", "world", "ann"]
        self.assertEqual(get_biggest_word(lst1), 'hello')

    def test_negative_empty_strings(self):
        lst1 =["","", ""]
        self.assertEqual(get_biggest_word(lst1), "")

    def test_negative_empty_list(self):
        lst1 =[]
        self.assertEqual(get_biggest_word(lst1), "List is empty")

class TestGetSumOfEvenListFunction(unittest.TestCase):
    def test_positive_all_numbres_are_even(self):
        lst1 = [2,-4, 8, 100]
        self.assertEqual(get_sum_of_even_list(lst1), 106)
    
    def test_positive_all_numbres_are_odd(self):
        lst1 = [2,-4, 8, 100]
        self.assertEqual(get_sum_of_even_list(lst1), 106)
    
    def test_positive_all_numbres_are_even(self):
        lst1 = [21,-3, 7, 101]
        self.assertEqual(get_sum_of_even_list(lst1), 0)
    
    def test_positive_some_numbres_are_even(self):
        lst1 = [21,-30, 78, 101]
        self.assertEqual(get_sum_of_even_list(lst1), 48)
    
    def test_positive_some_numbres_are_float(self):
        lst1 = [21.11,-30.34, 78.05, 102.0]
        self.assertEqual(get_sum_of_even_list(lst1), 102)

    def test_negative_empty_list(self):
        lst1 = []
        self.assertEqual(get_sum_of_even_list(lst1), "List is empty")

    

if __name__ == "__main__":
    unittest.main()
