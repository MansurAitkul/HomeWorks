import tkinter as tk
from tkinter import ttk
import requests
import json

def download_files():
    num_files = int(file_count.get())
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    data = data[:num_files]

    for i, post in enumerate(data):
        with open(f"file_{i + 1}.json", "w") as file:
            json.dump(post, file)

    status_label.config(text=f"Скачано {num_files} файлов")

window = tk.Tk()
window.title("Загрузка файлов")

frame = ttk.Frame(window)
frame.grid(row=0, column=0, padx=10, pady=10)

file_count_label = ttk.Label(frame, text="Количество файлов:")
file_count_label.grid(row=0, column=0, padx=5, pady=5)

file_count = ttk.Entry(frame)
file_count.grid(row=0, column=1, padx=5, pady=5)

download_button = ttk.Button(frame, text="Скачать файлы", command=download_files)
download_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

status_label = ttk.Label(frame, text="")
status_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
