import unittest

import task1

class Task1Test(unittest.TestCase):

    def test_most_frequent_length(self):
        input1 = ['a', 'ab', 'abc', 'cd', 'def', 'gh']
        output1 = ['ab', 'cd', 'gh']
        self.assertEqual(task1.most_frequent_length(input1), output1)

        input2 = []
        output2 = []
        self.assertEqual(task1.most_frequent_length(input2), output2)

        input3 = ['a']
        output3 = ['a']
        self.assertEqual(task1.most_frequent_length(input3), output3)


if __name__ == '__main__':
    unittest.main()
