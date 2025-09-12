def sum_negative_between_min_max(arr):
    """
    Находит сумму отрицательных элементов массива, расположенных между
    первым максимальным и первым минимальным элементами.
    """
    if len(arr) < 3:
        return 0

    # Находим значения и индексы минимального и максимального элементов
    min_val = min(arr)
    max_val = max(arr)

    # Обработка случая, когда все элементы одинаковы
    if min_val == max_val:
        return 0

    min_index = arr.index(min_val)
    max_index = arr.index(max_val)

    # Определяем границы среза
    start_index = min(min_index, max_index) + 1
    end_index = max(min_index, max_index)

    # Если диапазон пуст, возвращаем 0
    if start_index >= end_index:
        return 0

    # Суммируем отрицательные элементы в заданном диапазоне
    total_sum = 0
    for i in range(start_index, end_index):
        if arr[i] < 0:
            total_sum += arr[i]

    return total_sum

# Пример использования
my_array = [3, -2, 8, 10, -5, 1, -12, 4, 9]
# Минимальный элемент: -12 (индекс 6)
# Максимальный элемент: 10 (индекс 3)
# Элементы между ними: [-5, 1]
# Отрицательный элемент в диапазоне: -5
# Ожидаемый результат: -5

result = sum_negative_between_min_max(my_array)
print(f"Исходный массив: {my_array}")
print(f"Сумма отрицательных элементов между min и max: {result}")

another_array = [5, 2, -1, 10, -3, 8, 1, -9, 4]
# Минимальный элемент: -9 (индекс 7)
# Максимальный элемент: 10 (индекс 3)
# Элементы между ними: [-3, 8, 1]
# Отрицательный элемент в диапазоне: -3
# Ожидаемый результат: -3
result_2 = sum_negative_between_min_max(another_array)
print(f"Исходный массив: {another_array}")
print(f"Сумма отрицательных элементов между min и max: {result_2}")