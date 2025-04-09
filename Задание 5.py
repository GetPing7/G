''' Задание 5: Конвертация времени в 12-часовой формат '''

def convert_to_12_hour_format(hours, minutes):
    if hours == 0 or hours == 24:
        converted_hours = 12
        period = "AM"
    elif 1 <= hours <= 11:
        converted_hours = hours
        period = "AM"
    elif 12 <= hours <= 23:
        converted_hours = hours % 12
        period = "PM"
    else:
        raise ValueError("Неверный формат часов. Часы должны быть в диапазоне от 0 до 23.")

    formatted_minutes = f"{minutes:02d}"

    return f"{converted_hours}:{formatted_minutes} {period}"

print(convert_to_12_hour_format(0, 0))
print(convert_to_12_hour_format(14, 48))
print(convert_to_12_hour_format(21, 00))