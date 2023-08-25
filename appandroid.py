from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class RandomNumberGenerator(App):
    def generate_random_number(self, instance):
        random_number = random.randint(0, 100)
        self.random_number_label.text = f"Generated Number: {random_number}"

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.random_number_label = Label(text="Press the button to generate a random number", font_size=20)
        generate_button = Button(text="Generate Random Number", font_size=20)
        generate_button.bind(on_press=self.generate_random_number)
        layout.add_widget(self.random_number_label)
        layout.add_widget(generate_button)
        return layout

if __name__ == '__main__':
    RandomNumberGenerator().run()


########
# запуск приложения python main.py в терминале main.py
# помог нейросеть с первой функцией 