from app.product_mvp import percentage, price_calc


class TestProduct:
    def test_percentage(self, input_data_per):
        result = percentage(input_data_per[0], input_data_per[1])
        assert result == input_data_per[2]

    def test_price_calc(self, input_data_calc):
        result = price_calc(input_data_calc[0], input_data_calc[1], input_data_calc[2])
        assert result == f"Total price will be {input_data_calc[3]} USD"
