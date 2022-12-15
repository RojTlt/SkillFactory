per_cent={'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]
money=float(input("Введите сумму вклада "))
for stavka in per_cent.values():
    deposit.append(stavka*money)
print(deposit)
print('Максимальная сумма, которую вы сможете заработать - ',max(deposit))