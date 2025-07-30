from cProfile import label
from tkinter import *
from tkinter.messagebox import showinfo

import requests
from PIL import ImageTk, Image
from io import BytesIO



window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = Label()
label.pack(pady=10)

button = Button(window, text="Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()