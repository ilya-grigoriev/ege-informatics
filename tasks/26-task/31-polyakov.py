file = open('data/26-files/26-s1.txt')
file.readline()
prices = [int(line) for line in file]
prices.sort()

more_100 = [price for price in prices if price > 100]
less_100 = [price for price in prices if price <= 100]

sale = more_100[: len(more_100) // 2]   # Первая половина - маленькие цены. К ней магазину выгодно применять скидку
no_sale = more_100[len(more_100) // 2 :]  # Вторая половина - большие цены. К ней магазину невыгодно применять скидку

sum_sale = round(sum(sale) * 0.9)   # Находим сумму товаров, подходящих под скидку,
                                    # и применяем скидку для этой суммы с округлением (round).
# Нужно сделать именно так, а не использовать скидку для каждого товара.

print(sum(less_100) + sum_sale + sum(no_sale), max(sale))

file.close()
