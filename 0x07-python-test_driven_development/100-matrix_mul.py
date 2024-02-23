#!/usr/bin/python3
"""
Contains the matrix_mul function
"""
import unittest
from your_module_name import matrix_mul
class TestMatrixMul(unittest.TestCase):
    def test_matrix_mul(self):
        # Test case where matrices can be multiplied
        m_a = [[1, 2],[3, 4]]
        m_b = [[5, 6],[7, 8]]
        expected_result = [[19, 22],[43, 50]]
        self.assertEqual(matrix_mul(m_a, m_b), expected_result)

        # Test case where matrices cannot be multiplied
        m_a = [[1, 2, 3],
               [4, 5, 6]]
        m_b = [[7, 8],
               [9, 10],
               [11, 12]]
        with self.assertRaises(ValueError):
            matrix_mul(m_a, m_b)

        # Additional test cases can be added here

if __name__ == '__main__':
    unittest.main()
