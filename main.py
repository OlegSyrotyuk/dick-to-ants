def transform(count, uno, duo, many):
    mod10 = count % 10
    mod100 = count % 100
    if mod10 == 1 and mod100 != 11:
        return uno
    if 2 <= mod10 <= 4 and (mod100 < 10 or mod100 > 20):
        return duo
    return many


if __name__ == '__main__':
    dick = float(input("Введите размер своего члена: "))
    ants = dick * 2
    print(f'Размер вашего члена равен {ants} {transform(ants, "муравей", "муравья", "муравьев")}')
