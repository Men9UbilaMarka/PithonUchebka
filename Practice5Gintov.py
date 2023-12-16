def find_longest_word(file_path):
    # Открываем файл для чтения
    with open(file_path, 'r') as file:
        # Читаем содержимое файла и разделяем его на слова
        content = file.read()
        words = content.split()

        # Инициализируем переменную для хранения наиболее длинного слова
        longest_word = ''

        # Итерируемся по словам и обновляем наиболее длинное слово, если находим слово большей длины
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word

    return longest_word

# Пример использования программы
file_path = input("Введите путь к файлу: ")
longest_word = find_longest_word(file_path)
print("Наиболее длинное слово из файла:", longest_word)