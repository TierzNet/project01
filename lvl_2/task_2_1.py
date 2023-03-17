# Задача 2.1.

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# функции max и min использовать нельзя!

def minimum(arr):
    # начальное значение минимального значения - первый элемент списка
    min_val = arr[0]
    # проходим по всем элементам списка начиная со второго
    for i in range(1, len(arr)):
        # если текущий элемент меньше текущего минимального значения, обновляем минимальное значение
        if arr[i] < min_val:
            min_val = arr[i]
    # возвращаем минимальное значение
    return min_val

def maximum(arr):
    # начальное значение максимального значения - первый элемент списка
    max_val = arr[0]
    # проходим по всем элементам списка начиная со второго
    for i in range(1, len(arr)):
        # если текущий элемент больше текущего минимального значения, обновляем минимальное значение
        if arr[i] > max_val:
            max_val = arr[i]
    # возвращаем максимальное значение
    return max_val

arr1 = [4,6,2,1,9,63,-134,566]
print("Minimum value:", minimum(arr1))  # -134
print("Maximum value:", maximum(arr1))  # 566

arr2 = [-52, 56, 30, 29, -54, 0, -110]
print("Minimum value:", minimum(arr2))  # -110
print("Maximum value:", maximum(arr2))  # 56

arr3 = [42, 54, 65, 87, 0]
print("Minimum value:", minimum(arr3))  # 0
print("Maximum value:", maximum(arr3))  # 87

arr4 = [5]
print("Minimum value:", minimum(arr4))  # 5
print("Maximum value:", maximum(arr4))  # 5