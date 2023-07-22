

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

    total_price = 0
    for item, count in item_count.items():
        if item in special_offer_prices:
            offer_count, offer_price = special_offer_prices[item]
            offers_number = count // offer_count
            print(offers_number)
            remaining_count = count % offer_count
            print(remaining_count)
            total_price = offers_number * offer_price + remaining_count * prices[item]
        else:
            total_price += count * prices[item]

    return total_price


