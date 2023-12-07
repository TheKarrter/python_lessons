import tkinter as tk
import reader

class Window:
    def __init__(self, links):
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title('Прогноз погоды')
        self.check = []
        self.label = tk.Label(self.root, wraplength= 800, font = ('Trebuchet MS', 11))
        self.label.grid(row = 0, column = 0, columnspan = 2)
        
        self.set_text(links)

        self.entry = tk.Entry(self.root, width = 50)
        self.entry.grid(row = 1, column = 0, sticky='E')

        self.button = tk.Button(self.root, text = 'Ввод', command = lambda x=links:self.check_input(x))
        self.button.grid(row=1, column=1, sticky='W')
    def set_text(self, links):
        text = ''
        for city in links:
            self.check.append(city)
            text += city + ', '
        text = text[:-2]
        self.label.configure(text = text)
    def check_input(self, links):
        choice = self.entry.get()
        if choice not in self.check:
            return
        self.parse_weather(links[choice])
    def parse_weather(self, links):
        w = reader.Weather(links)
        data = w.soup.find('div', {'id':'archiveString'})
        temp = data.find('span', {'class': 't_0'}).text
        text = data.find('a', {'class':'ArchiveStrLink'})
        if text is None:
            text = data.find('div', {'class':'ArchiveInfo'})
        text.text.replace('Архив погоды на метеостанции', '')
        self.label.configure(text = temp + '\n' + text.text)
    def run(self):
        self.root.mainloop()