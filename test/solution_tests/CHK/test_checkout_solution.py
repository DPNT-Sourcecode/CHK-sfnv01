from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_single_item_checkout(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('D') == 15

    def test_offer_checkout(self):
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('BBB') == 75
        assert checkout_solution.checkout('AAABBCD') == 210
        assert checkout_solution.checkout('AAABBBD') == 220

    def test_wrong_input_checkout(self):
        assert checkout_solution.checkout('Z') == -1

    def test_free_item_checkout(self):
        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('EEBB') == 110
        assert checkout_solution.checkout('AAAAABBEEB') == 325
