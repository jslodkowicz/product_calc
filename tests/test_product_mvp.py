from app.product_mvp import percentage, price_calc
import unittest
from unittest.mock import patch

class TestProduct(unittest.TestCase):

    def test_percentage(self):
        self.assertEqual(percentage(100, 1), 1)
        self.assertEqual(percentage(5000, 20), 1000)

    # @patch('builtins.input', side_effect=[10, 10, 'UT'])
    def test_price_calc_no_discount(self, mock_inputs):
        result = price_calc()
        self.assertEqual(result, 'Total price will be 106.85 USD')

    # @patch('builtins.input', side_effect=[7, 1000, 'ca'])
    def test_price_calc_with_discount(self, mock_inputs):
        result = price_calc()
        self.assertEqual(result, 'Total price will be 7047.07 USD')

    # @patch('builtins.input', side_effect=[8, 30, 'WRONG'])
    def test_price_calc_error(self, mock_inputs):
        price_calc()
        self.assertRaises(KeyError)


if __name__ == '__main__':
    unittest.main(verbosity=2)
