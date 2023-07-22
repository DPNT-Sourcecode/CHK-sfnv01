

# noinspection PyUnusedLocal
# skus = unicode string

prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
special_offer_prices = {"A": [(5, 200),(3, 130)], "B": [(2, 45)]}
special_free_items = {"E": ("B", 2), "F": ("F", 2)}
def checkout(skus):
    items = prices.keys()
    item_count = {key: 0 for key in items}

    for item in skus:
        if item not in item_count:
            return -1
        item_count[item] += 1

    total_price = 0
    for item, count in item_count.items():
        if item in special_free_items:
            free_item, free_item_count = special_free_items[item]
            free_items = item_count[item] // free_item_count
            if item == 'F' and count < 3:
                continue
            item_count[free_item] = max(0, item_count[free_item] - free_items)
    for item, count in item_count.items():
        if item in special_offer_prices:
            for offer_count, offer_price in special_offer_prices[item]:
                offers_number = count // offer_count
                count -= offers_number * offer_count
                total_price += offers_number * offer_price
        total_price += count * prices[item]

    return total_price

