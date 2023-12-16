def print_list(lst):
    print(*lst, sep=';')

# Ввод списка
user_input = input("Введите элементы списка через пробел: ")
input_list = user_input.split()

# Вызов функции
print_list(input_list)