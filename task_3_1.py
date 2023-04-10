# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступны следующие методы матрицы:
#       * принимать новые значения,
#       * заменять существующие значения,
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание!
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows  # количество строк
        self.cols = cols  # количество столбцов
        self.matrix = [[None for j in range(cols)] for i in range(rows)]  # создаем пустую матрицу заданных размеров

        # Заполняем матрицу изначальными значениями
        for i in range(rows):
            for j in range(cols):
                self.set_value(i, j, 1)

    def set_value(self, row, col, value):
        if row < 0 or col < 0:
            raise ValueError("Row and column indices must be non-negative")

        # Если индексы находятся за границами матрицы, расширяем матрицу
        while row >= self.rows:
            self.matrix.append([1 for j in range(self.cols)])
            self.rows += 1
        while col >= self.cols:
            for i in range(self.rows):
                self.matrix[i].append(None)
            self.cols += 1

        self.matrix[row][col] = value  # устанавливаем значение в заданную ячейку

    def replace_value(self, row, col, value):
        self.set_value(row, col, value)

    def get_rows_count(self):
        return self.rows

    def get_cols_count(self):
        return self.cols

    def __str__(self):
        return '\n'.join([str(row) for row in self.matrix])


# Создание матрицы 10 на 10 из единиц
m = Matrix(10, 10)

# Вывод матрицы
print("Созданная матрица:")
print(m)
# Вывод количества строк и столбцов
print("Количество строк:", m.get_rows_count(), "Количество столбцов:", m.get_cols_count())

# Установка новых значений
m.set_value(10, 3, 5)
m.set_value(3, 2, 8)
m.set_value(11, 8, None)
m.replace_value(3, 4, 7)
m.replace_value(6, 1, 2)
m.replace_value(6, 5, None)

print("Матрица после использования методов добавления и замены:")
print(m)

# Вывод количества строк и столбцов
print("Количество строк:", m.get_rows_count(), "Количество столбцов:", m.get_cols_count())

# Да, есть еще вариант через создания словарей
class Table:
    def __init__(self, colnames: list):
        self.colnames = colnames
        self.rows = []

    def add_row(self, row: dict):
        if any(colname not in tuple(row) for colname in self.colnames):  # хотя бы один элемент не соответствует
            print('Такой колонки нет')
        else:
            self.rows.append(row)

    def get_column(self, colname):
        if (colname not in self.colnames):
            print('Такой колонки нет')
        return [r[colname] for r in self.rows]


    def sum(self, colname: str):
        if colname not in self.colnames:
          print('Неправильный формат')
        return sum([r[colname] for r in self.rows])



table1 = Table([1, 2])
table1.add_row({1: 10, 2: 20})
table1.add_row({1: 20, 2: 400})
table1.add_row({1: 30, 2: 600})
table1.add_row({1: 40, 2: 800})
print(table1.get_column(1))
print(table1.get_column(2))
print(table1.rows)
