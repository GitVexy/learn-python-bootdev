def purchase_item(price, gold_available):
    if price <= gold_available:
        return gold_available - price
    else:
        raise Exception("not enough gold")
