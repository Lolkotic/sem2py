month_dict = {'Зима':  [12, 1, 2],
              'Весна': [3, 4, 5],
              'Лето':  [6, 7, 8],
              'Осень': [9, 10, 11]}

month_num = int(input('Введите порядковый номер месяца: '))
for i in month_dict.items():
    if month_num in i[1]:
        print(f'Введенный номер месяца относится к сезону {i[0]}')