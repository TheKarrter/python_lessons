from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import requests



class Application(App):
    def build(self):

        button_together = BoxLayout()
        grid = GridLayout(cols = 1)
        
        my_button = Button(text = "Нажми меня", font_size = 30, background_color = 'cyan')
        my_button_2 = Button(text = 'Меня жмать не надо', font_size = 30, background_color = 'cyan')
        label = Label(text = "Текст", font_size = 30)

        button_together.add_widget(my_button)
        button_together.add_widget(my_button_2)

        grid.add_widget(label)
        grid.add_widget(button_together)

        return grid

if __name__ == "__main__":
    Application().run()