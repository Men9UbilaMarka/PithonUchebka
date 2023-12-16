def double_elements():
    # Ввод списка чисел от пользователя
    user_input = input("Введите числа, разделенные пробелами: ")
    lst = [int(x) for x in user_input.split()]

    # Создание и возврат нового списка с удвоенными элементами
    return [x * 2 for x in lst]


# Пример использования функции
doubled_list = double_elements()
print(doubled_list)