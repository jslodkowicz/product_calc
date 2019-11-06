def percentage(val, per):
    return val/100*per


def price_calc(quantity, price, state):

    tax = {'UT':6.85, 'NV':8.00, 'TX':6.25, 'AL':4.00, 'CA':8.25}
    discount = {50000: 15, 10000: 10, 7000: 7, 5000: 5, 1000: 3}

    overall_price = price * quantity

    disc = [discount[key] for key in discount if overall_price >= key]
    if not disc:
        overall_price = overall_price
    else:
        overall_price -= percentage(overall_price, max(disc))

    if state not in tax:
        return KeyError("Your state code doesn't match any value")

    final_price = overall_price + percentage(overall_price, tax[state])

    return f'Total price will be {round(final_price, 2)} USD'


if __name__ == '__main__':
    print(price_calc())
