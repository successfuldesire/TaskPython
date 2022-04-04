price_1 = [57.8, 46.51, 97, 5.4]
new_price = []
for price_2 in price_1:
    rub = int(price_2)
    kop = round((price_2 - rub) * 100)
    new_price.append(f' {rub}, рублей, {kop}, копеек')
print(", ".join(new_price))
id_2 = id(price_1)
price_1.sort()
print(price_1)
print(id(price_1) == id_2)
new_price = sorted(price_1, reverse=True)
print(new_price)
