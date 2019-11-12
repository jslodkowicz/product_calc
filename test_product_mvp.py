from app.product_mvp import percentage, price_calc
import unittest


class TestProduct(unittest.TestCase):
    def test_percentage(self):
        self.assertEqual(percentage(100, 1), 1)
        self.assertEqual(percentage(5000, 20), 1000)

    def test_price_calc_no_discount(self):
        result = price_calc(10, 10, "UT")
        self.assertEqual(result, "Total price will be 106.85 USD")

    def test_price_calc_with_discount(self):
        result = price_calc(7, 1000, "CA")
        self.assertEqual(result, "Total price will be 7047.07 USD")

    def test_price_calc_error(self):
        price_calc(8, 30, "WRONG")
        self.assertRaises(KeyError)


if __name__ == "__main__":
    unittest.main(verbosity=2)
