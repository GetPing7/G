''' Задание 3: Фильтрация массива по заданному критерию '''

def filter_greater_than(s, threshold):
    result = []
    for num in s:
        if num > threshold:
            result.append(num)
    return result

print(filter_greater_than([1, 5, 8, 3, 10], 5))
print(filter_greater_than([0, 1, 2, 4, 8, 16, 32], 4))