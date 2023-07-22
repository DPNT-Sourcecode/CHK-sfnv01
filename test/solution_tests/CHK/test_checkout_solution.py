from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        # assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('D') == 15
        # assert checkout_solution.checkout('ABCD') == 115
        # assert checkout_solution.checkout('ABCD') == 115
        # assert checkout_solution.checkout('ABCD') == 115


