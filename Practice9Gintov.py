import tkinter as tk
import tkinter.filedialog
from PIL import Image, ImageEnhance, ImageFilter
import pyscreenshot as ImageGrab
from PIL import ImageTk

class ScreenshotApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Screenshot App")

        self.screenshot_image = None
        self.configured_image = None

        self.create_widgets()

    def create_widgets(self):
        # Создание кнопки "Сделать скриншот"
        self.screenshot_button = tk.Button(self.master, text="Сделать скриншот", command=self.take_screenshot)
        self.screenshot_button.pack()

        # Создание ползунка для настройки яркости
        self.brightness_scale = tk.Scale(self.master, from_=0.1, to=2, resolution=0.1, label="Яркость",
                                         orient=tk.HORIZONTAL)
        self.brightness_scale.pack()

        # Создание кнопки для применения настроек
        self.apply_button = tk.Button(self.master, text="Применить", command=self.apply_config)
        self.apply_button.pack()

        # Создание выпадающего списка с фильтрами
        self.filter_var = tk.StringVar()
        self.filter_dropdown = tk.OptionMenu(self.master, self.filter_var, "Размытие", "Резкость", "Черно-белое")
        self.filter_dropdown.pack()

        # Создание кнопки для поворота изображения
        self.rotate_button = tk.Button(self.master, text="Повернуть", command=self.rotate_image)
        self.rotate_button.pack()

        # Создание кнопки "Сохранить"
        self.save_button = tk.Button(self.master, text="Сохранить", command=self.save_image)
        self.save_button.pack()

    def take_screenshot(self):
        # Сделать скриншот экрана и сохранить его в переменной
        self.screenshot_image = ImageGrab.grab()

        # Преобразовать изображение в формат, совместимый с Tkinter
        self.screenshot_image = ImageTk.PhotoImage(self.screenshot_image)

        # Создать и отобразить на экране Label с скриншотом
        self.screenshot_label = tk.Label(self.master, image=self.screenshot_image)
        self.screenshot_label.pack()

    def apply_config(self):
        if self.screenshot_image:
            # Создать копию скриншота
            self.configured_image = self.screenshot_image.copy()

            # Получить сырое изображение из PhotoImage объекта
            raw_image = self.screenshot_image.tkinter_image

            # Создать объект Image из сырого изображения
            image = ImageTk.getimage(raw_image)

            # Изменить яркость согласно установленному значению
            brightness_value = self.brightness_scale.get()
            enhancer = ImageEnhance.Brightness(image)
            modified_image = enhancer.enhance(brightness_value)

            # Применить выбранный фильтр
            filter_option = self.filter_var.get()
            if filter_option == "Размытие":
                modified_image = modified_image.filter(ImageFilter.BLUR)
            elif filter_option == "Резкость":
                modified_image = modified_image.filter(ImageFilter.SHARPEN)
            elif filter_option == "Черно-белое":
                modified_image = modified_image.convert("L")

            # Создать PhotoImage объект из измененного изображения
            self.configured_image = ImageTk.PhotoImage(modified_image)

            # Обновить изображение на Label
            self.screenshot_label.config(image=self.configured_image)

    def rotate_image(self):
        if self.configured_image:
            # Получить сырое изображение из PhotoImage объекта
            raw_image = self.configured_image.tkinter_image

            # Создать объект Image из сырого изображения
            image = ImageTk.getimage(raw_image)

            # Повернуть изображение на 90 градусов по часовой стрелке
            rotated_image = image.rotate(-90)

            # Создать PhotoImage объект из повернутого изображения
            self.configured_image = ImageTk.PhotoImage(rotated_image)

            # Обновить изображение на Label
            self.screenshot_label.config(image=self.configured_image)

    def save_image(self):
        if self.configured_image:
            # Открыть диалоговое окно для сохранения файла
            file_path = tk.filedialog.asksaveasfilename(defaultextension=".png",
                                                        filetypes=(("PNG Files", "*.png"), ("All Files", "*.*")))
            if file_path:
                # Сохранить сконфигурированное изображение
                self.configured_image.write(file_path)

# Создание главного окна приложения
root = tk.Tk()

# Создание экземпляра класса ScreenshotApp и запуск приложения
app = ScreenshotApp(master=root)
app.mainloop()