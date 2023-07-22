# noinspection PyUnusedLocal
# skus = unicode string

prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
    "F": 10,
    "G": 20,
    "H": 10,
    "I": 35,
    "J": 60,
    "K": 80,
    "L": 90,
    "M": 15,
    "N": 40,
    "O": 10,
    "P": 50,
    "Q": 30,
    "R": 50,
    "S": 30,
    "T": 20,
    "U": 40,
    "V": 50,
    "W": 20,
    "X": 90,
    "Y": 10,
    "Z": 50,
}
special_offer_prices = {
    "A": [(5, 200), (3, 130)],
    "B": [(2, 45)],
    "H": [(5, 45), (10, 80)],
    "K": [(2, 150)],
    "P": [(5, 200)],
    "Q": [(3, 80)],
    "V": [(2, 90), (3, 130)],
}
special_free_items = {
    "E": ("B", 2),
    "F": ("F", 2),
    "N": ("M", 3),
    "R": ("Q", 3),
    "U": ("U", 3),
}


def checkout(skus):
    items = prices.keys()
    item_count = {key: 0 for key in items}

    if not isinstance(skus, str):
        return -1

    for item in skus:
        if item not in item_count:
            return -1
        item_count[item] += 1

    total_price = 0
    for item, count in item_count.items():
        if item in special_free_items:
            free_item, free_item_count = special_free_items[item]
            if free_item == item:
                free_items = item_count[item] // (free_item_count + 1)
            else:
                free_items = item_count[item] // free_item_count
            item_count[free_item] = max(0, item_count[free_item] - free_items)
    for item, count in item_count.items():
        if item in special_offer_prices:
            for offer_count, offer_price in special_offer_prices[item]:
                offers_number = count // offer_count
                count -= offers_number * offer_count
                total_price += offers_number * offer_price
        total_price += count * prices[item]

    return total_price


