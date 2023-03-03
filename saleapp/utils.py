

def cart_stats(list):
    total_price, total_quantity = 0, 0
    if list:
        for c in list.values():
            total_quantity += 1
            total_price += c['price']

    return {
        'total_price': total_price,
        'total_quantity': total_quantity
    }