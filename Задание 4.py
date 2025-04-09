''' Задание 4: Поиск максимального и минимального элемента в массиве '''

def find_min_max(s):
    if not s:
        return ("Error: The list is empty.")

    min_val = max_val = s[0]

    for num in s:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return (min_val, max_val)

print(find_min_max([3, 1, 0, 9, 5, 11]))
print(find_min_max([]))