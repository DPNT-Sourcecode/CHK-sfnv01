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
        assert checkout_solution.checkout(1) == -1
        assert checkout_solution.checkout([]) == -1

    def test_free_different_item_checkout(self):
        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('EEBB') == 110
        assert checkout_solution.checkout('AAAAABBEEB') == 325

    def test_free_same_item_checkout(self):
        assert checkout_solution.checkout('FFF') == 20
        assert checkout_solution.checkout('FF') == 20
        assert checkout_solution.checkout('FFFFFF') == 40
        assert checkout_solution.checkout('FFFFFFFFFF') == 70

    def test_full_inventory_checkout(self):
        assert checkout_solution.checkout('AAAAABBBCEEFFFHHHHHHHHHHMNNN') == 565

    def test_group_discount_checkout(self):
        assert checkout_solution.checkout('STX') == 45
        assert checkout_solution.checkout('STXYZ') == 82
        assert checkout_solution.checkout('STXSTX') == 90
        assert checkout_solution.checkout('SSS') == 45
        assert checkout_solution.checkout('SSSTX') == 82
        assert checkout_solution.checkout('SSSTXYZ') == 107
        assert checkout_solution.checkout('STXS') == 62
        assert checkout_solution.checkout('SSSZ') == 65
        assert checkout_solution.checkout('ZZZS') == 65