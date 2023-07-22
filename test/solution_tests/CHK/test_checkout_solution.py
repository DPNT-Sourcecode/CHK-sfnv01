from lib.solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('D') == 15
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('BBB') == 75
        assert checkout_solution.checkout('AAABBCD') == 210
        assert checkout_solution.checkout('AAABBBD') == 220
        assert checkout_solution.checkout('E') == -1
