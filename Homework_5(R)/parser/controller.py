import view
import reader

def main():
    link = "https://rp5.ru/Погода_в_России"
    weather = reader.Weather(link)
    window = view.Window(weather.get_cities())
    window.run()

