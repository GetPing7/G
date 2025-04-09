''' Задание 2: Подсчёт уникальных символов в строке '''

def count_unique_chars(s):
    unique_chars = set(s)
    return len(unique_chars)

print(count_unique_chars("hello"))
print(count_unique_chars("aabbcc"))