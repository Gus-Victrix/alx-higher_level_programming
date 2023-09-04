#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

"""
Unittest for the max_integer function
"""


class TestFnMaxInt(unittest.TestCase):
    """
    Class for the test unit
    Arg:
        unittest.TestCase (Conventional)
    Methods:
        test_globalDoc: Test the global doc of the file
        test_functionDoc: Test the function doc
        test_emptyList: Test the function with an empty list arg
        test_noArg: Test the fucntion with no arg given
        test_usualCase: With a commun list
        test_maxBegin: The max is at the begin of the list
        test_maxEnd: The max is at the end of the list
        test_negativNums: Test with negativ nums in the list
        test_onlyNegativNums: Test with only negativ nums
        test_multipleMax: Test with mulptiple max in the list
        test_stringArg: Test with a sting passed in arg
        test_noneArg: Test with None arg
        test_listContainString: Test with a list that contain a string
        test_intArg: Test with a int passed in arg

        Methods do not return anything.
    Return: Nothing
    """
    def test_globalDoc(self):
        str = (__import__("6-max_integer").__doc__)
        self.assertGreater(len(str), 1)

    def test_functionDoc(self):
        str = (__import__("6-max_integer").max_integer.__doc__)
        self.assertGreater(len(str), 1)

    def test_emptyList(self):
        self.assertEqual(max_integer([]), None)

    def test_noArg(self):
        self.assertEqual(max_integer(), None)

    def test_usualCase(self):
        numsContainer = [1, 3, 34, 4, 32, 76, 23, 30]
        self.assertEqual(max_integer(numsContainer), 76)

    def test_maxBegin(self):
        numsContainer = [76, 3, 34, 4, 32, 1, 23, 30]
        self.assertEqual(max_integer(numsContainer), 76)

    def test_maxEnd(self):
        numsContainer = [1, 3, 34, 4, 32, 30, 23, 76]
        self.assertEqual(max_integer(numsContainer), 76)

    def test_oneInt(self):
        numsContainer = [1]
        self.assertEqual(max_integer(numsContainer), 1)

    def test_negativNums(self):
        numsContainer = [1, 3, 34, -4, 32, -30, 23, 76]
        self.assertEqual(max_integer(numsContainer), 76)

    def test_onlyNegativNums(self):
        numsContainer = [-1, -3, -34, -4, -32, -30, -23, -76]
        self.assertEqual(max_integer(numsContainer), -1)

    def test_multipleMax(self):
        numsContainer = [3, 76, 34, 76, 32, 76, 23, 30]
        self.assertEqual(max_integer(numsContainer), 76)

    def test_stringArg(self):
        self.assertEqual(max_integer("Shool"), "o")

    def test_noneArg(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_listContainString(self):
        falseNumsContainer = [76, 3, 34, 4, "School", 1, 23, 30]
        with self.assertRaises(TypeError):
            max_integer(falseNumsContainer)

    def test_intArg(self):
        with self.assertRaises(TypeError):
            max_integer(3)


if __name__ == "__main__":
    unittest.main()
