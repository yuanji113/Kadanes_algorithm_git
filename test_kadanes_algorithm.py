from unittest import TestCase
import kadanes_algorithm

class Test(TestCase):

    def setUp(self):
        self.test_arr_1 = [1, -3, 2, 3, -4]
        self.test_arr_1_res = 5

        self.test_arr_2 = [2, -5, 1, -4, 3, -2]
        self.test_arr_2_res = -8

    def test_find_max_con_sub_sum(self):
        self.assertEqual(kadanes_algorithm.find_max_con_sub_sum(self.test_arr_1), self.test_arr_1_res)

    def test_find_min_con_sub_sum(self):
        self.assertEqual(kadanes_algorithm.find_min_con_sub_sum(self.test_arr_2), self.test_arr_2_res)

