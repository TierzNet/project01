# Задача 2.2.

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например:
# месяц 2 (февраль) является частью первого квартала;
# месяц 6 (июнь) является частью второго квартала;
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    pass
def quarter_of(month):
    if month < 1 or month > 12:
        # если месяц не входит в диапазон от 1 до 12, вызываем ошибку
        raise ValueError("Invalid month number")

    # расчет номера квартала по номеру месяца
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    else:
        return 4

# Ввод номера месяца с клавиатуры
month = int(input("Введите номер месяца (от 1 до 12): "))
quarter = quarter_of(month)

print("Квартал:", quarter)