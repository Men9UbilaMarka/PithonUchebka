from datetime import datetime, timedelta

def get_future_date(x):
    # Получение текущей даты
    current_date = datetime.now()

    # Прибавление года к текущей дате
    future_date = current_date + timedelta(days=x*365)

    return future_date

# Пример использования функции
years_to_add = int(input("Введите количество лет для прибавления: "))
future_date = get_future_date(years_to_add)
print("Будущая дата:", future_date)