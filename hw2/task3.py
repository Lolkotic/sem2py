# 3) Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

n = int(input("Введите номер месяца:"))
matrix = ["зима", "весна", "лето", "осень"]
if n <= 3:
    print(f"Сезон Вашего месяца - {matrix[0]}")
if 3 < n <= 5:
    print(f"Сезон Вашего месяца - {matrix[1]}")
if 5 < n <= 8:
    print(f"Сезон Вашего месяца - {matrix[2]}")
if 8 < n <= 12:
    print(f"Сезон Вашего месяца - {matrix[0]}")
if n > 12 or n <= 0:
    print(f"\nНеправильное число \n\tВведите число от 1 до 12")





