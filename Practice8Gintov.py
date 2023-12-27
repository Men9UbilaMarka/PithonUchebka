from PIL import Image
from PIL import ImageOps
import os

def apply_autocontrast(image_path):
    # Открываем изображение
    image = Image.open(image_path)

    # Применяем операцию авто контраста
    autocontrast_image = ImageOps.autocontrast(image)

    # Составляем новое имя файла с префиксом
    new_name = "autocontrast_" + os.path.basename(image_path)

    # Комбинируем новое имя с директорией
    new_image_path = os.path.join(os.path.dirname(image_path), new_name)

    # Сохраняем новое изображение с новым именем
    autocontrast_image.save(new_image_path)

# Пример использования
image_path = "C:/Users/МЕНЯ УБИЛА МАРКА/PycharmProjects/pythonProject/PythonPractice/Practice 8/VO2XrS-F93M.jpg"
apply_autocontrast(image_path)