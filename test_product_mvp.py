from app.product_mvp import percentage, price_calc


class TestProduct:
    def test_percentage(self):
        assert percentage(100, 1) == 1
        assert percentage(5000, 20) == 1000
        assert percentage(10, 5) == 0.5

    def test_price_calc_no_discount(self):
        res_1 = price_calc(10, 10, "UT")
        res_2 = price_calc(30, 15, "TX")
        res_3 = price_calc(200, 3.99, "NV")
        assert res_1 == "Total price will be 106.85 USD"
        assert res_2 == "Total price will be 478.12 USD"
        assert res_3 == "Total price will be 861.84 USD"

    def test_price_calc_with_discount(self):
        res_1 = price_calc(7, 1000, "CA")
        res_2 = price_calc(100, 20, "TX")
        res_3 = price_calc(1000, 50, "AL")
        assert res_1 == "Total price will be 7047.07 USD"
        assert res_2 == "Total price will be 2061.25 USD"
        assert res_3 == "Total price will be 44200.0 USD"
