

# noinspection PyUnusedLocal
# skus = unicode string

prices = {"A": 50, "B": 30, "C": 20, "D": 15}
special_offer_prices = {"A": (3, 130), "B": (2, 45)}
def checkout(skus):
    skus = prices.keys()
    item_count = {key: 0 for key in skus}

    for item in skus:
        if item not in item_count:
            return -1
        item_count[item] += 1


