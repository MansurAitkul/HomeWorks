import sys
import os
import requests
import asyncio
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Загрузка изображений")
        self.setGeometry(300, 300, 250, 150)

        self.sync_button = QPushButton("Синхронная загрузка", self)
        self.sync_button.clicked.connect(self.sync_download)
        self.sync_button.setGeometry(30, 30, 190, 30)

        self.async_button = QPushButton("Асинхронная загрузка", self)
        self.async_button.clicked.connect(self.async_download)
        self.async_button.setGeometry(30, 70, 190, 30)

    def download_image(self, url, filename):
        response = requests.get(url)
        with open(filename, "wb") as file:
            file.write(response.content)

    def sync_download(self):
        folder_path = "images_sync"
        os.makedirs(folder_path, exist_ok=True)
        urls = [
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            
        ]

        for i, url in enumerate(urls):
            filename = os.path.join(folder_path, f"image{i + 1}.jpg")
            self.download_image(url, filename)

        print("Синхронная загрузка завершена.")

    async def async_download_image(self, url, filename):
        response = await self.loop.run_in_executor(None, requests.get, url)
        with open(filename, "wb") as file:
            file.write(response.content)

    async def async_download(self):
        folder_path = "images_async"
        os.makedirs(folder_path, exist_ok=True)
        urls = [
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            "https://shapka-youtube.ru/kartinka-s-nadpisyu-abonent-nedostupen/",
            
        ]

        self.loop = asyncio.get_running_loop()
        tasks = [self.async_download_image(url, os.path.join(folder_path, f"image{i + 1}.jpg")) for i, url in enumerate(urls)]
        await asyncio.gather(*tasks)

        print("Асинхронная загрузка завершена.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
