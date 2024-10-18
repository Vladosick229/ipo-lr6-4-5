import random

# Создание списка случайных целых чисел от -50 до 50 размером 25 элементов
numbers = [random.randint(-50, 50) for _ in range(25)]

# Инициализация счетчиков
positive_count = 0
negative_count = 0
zero_count = 0

# Подсчет количества положительных, отрицательных и нулевых элементов
for number in numbers:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    else:
        zero_count += 1

# Расчет процентов
total_count = len(numbers)
positive_percentage = (positive_count / total_count) * 100
negative_percentage = (negative_count / total_count) * 100
zero_percentage = (zero_count / total_count) * 100

# Нахождение самого большого и самого маленького значения
max_value = max(numbers)
min_value = min(numbers)

# Вывод результатов
print("Список чисел:")
print(numbers)
print("\nРезультаты:")
print(f"Положительные числа: {positive_count} ({positive_percentage}%)")
print(f"Отрицательные числа: {negative_count} ({negative_percentage}%)")
print(f"Нули: {zero_count} ({zero_percentage}%)")
print(f"\nСамое большое значение: {max_value}")
print(f"Самое маленькое значение: {min_value}")
