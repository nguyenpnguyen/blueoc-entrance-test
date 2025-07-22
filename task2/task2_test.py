import unittest

import task2

class Task2Test(unittest.TestCase):

    def test_sum_two_largest_ints(self):
        input1 = [1, 4, 2, 3, 5]
        output1 = 9
        self.assertEqual(task2.sum_two_largest_ints(input1), output1)

        input2 = [3]
        output2 = 3
        self.assertEqual(task2.sum_two_largest_ints(input2), output2)

        input3 = [1, 2, 3, 4, 5, 5]
        output3 = 10 
        self.assertEqual(task2.sum_two_largest_ints(input3), output3)

        input4 = []
        self.assertRaises(ValueError, task2.sum_two_largest_ints, input4)

        input5 = [-10, -5, 5]
        output5 = 0
        self.assertEqual(task2.sum_two_largest_ints(input5), output5)


if __name__ == '__main__':
    unittest.main()
