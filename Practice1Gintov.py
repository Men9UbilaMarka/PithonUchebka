numbers = input("Введите список чисел через пробел: ")
numbers = numbers.split()
numbers = [int(num) for num in numbers]
reversed_list = [numbers[2], numbers[1], numbers[0]]
print(reversed_list)
